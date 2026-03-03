from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json
import random

from .forms import (
	Step1BasicForm,
	Step2BackgroundForm,
	Step3AbilitiesForm,
	Step4CombatForm,
	Step5SkillsForm,
	Step6EquipmentForm,
)
from .models import CharacterCreator
from django.contrib.auth.decorators import login_required


SESSION_KEY = 'character_creation'


def _get_session_data(request):
	return request.session.get(SESSION_KEY, {})


def _save_session_data(request, data: dict):
	sess = _get_session_data(request)
	sess.update(data)
	request.session[SESSION_KEY] = sess


def start_creation(request):
	# clear any previous data and start at step 1
	if SESSION_KEY in request.session:
		del request.session[SESSION_KEY]
	return redirect('charactercreator:step1')


def step1_basic(request):
	data = _get_session_data(request)
	if request.method == 'POST':
		form = Step1BasicForm(request.POST)
		if form.is_valid():
			_save_session_data(request, form.cleaned_data)
			return redirect('charactercreator:step2')
	else:
		form = Step1BasicForm(initial={k: data.get(k) for k in ['char_name', 'char_Race', 'char_class', 'char_Alignment', 'char_level']})
	return render(request, 'charactercreator/step_form.html', {'form': form, 'step': 1, 'title': 'Basic Info'})


def step2_background(request):
	data = _get_session_data(request)
	if request.method == 'POST':
		form = Step2BackgroundForm(request.POST)
		if form.is_valid():
			_save_session_data(request, form.cleaned_data)
			return redirect('charactercreator:step3')
	else:
		form = Step2BackgroundForm(initial={k: data.get(k) for k in ['char_Background', 'char_Background_Ability']})
	return render(request, 'charactercreator/step_form.html', {'form': form, 'step': 2, 'title': 'Background'})


def step3_abilities(request):
	data = _get_session_data(request)
	# support rolling stats via GET ?roll=1 (4d6 drop lowest, repeated 6 times)
	def _roll_4d6_drop_lowest():
		rolls = [random.randint(1, 6) for _ in range(4)]
		return sum(rolls) - min(rolls)

	if request.method == 'POST':
		form = Step3AbilitiesForm(request.POST, char_class=data.get('char_class'))
		if form.is_valid():
			_save_session_data(request, form.cleaned_data)
			return redirect('charactercreator:step4')
	else:
		# check for roll request
		if request.GET.get('roll'):
			rolled = [_roll_4d6_drop_lowest() for _ in range(6)]
			# map rolled values to ability order: Str, Dex, Con, Int, Wis, Cha
			initial = {
				'char_Strength': rolled[0],
				'char_Dexterity': rolled[1],
				'char_Constitution': rolled[2],
				'char_Intelligence': rolled[3],
				'char_Wisdom': rolled[4],
				'char_Charisma': rolled[5],
			}
		else:
			initial = {k: data.get(k) for k in ['char_Strength', 'char_Dexterity', 'char_Constitution', 'char_Intelligence', 'char_Wisdom', 'char_Charisma']}
		form = Step3AbilitiesForm(initial=initial, char_class=data.get('char_class'))
	return render(request, 'charactercreator/step_form.html', {'form': form, 'step': 3, 'title': 'Abilities'})


def step4_combat(request):
	data = _get_session_data(request)
	if request.method == 'POST':
		form = Step4CombatForm(request.POST, char_class=data.get('char_class'))
		if form.is_valid():
			_save_session_data(request, form.cleaned_data)
			return redirect('charactercreator:step5')
	else:
		# build smarter defaults using earlier selections (class, level, ability scores)
		defaults = {}
		cls = data.get('char_class')
		class_defaults = None
		if cls:
			# import CLASS_DEFAULTS from forms to reuse mapping
			try:
				from .forms import CLASS_DEFAULTS
				class_defaults = CLASS_DEFAULTS.get(cls)
			except Exception:
				class_defaults = None

		# base hit die and speed from class defaults
		if class_defaults:
			defaults['char_Hit_Die'] = class_defaults.get('hit_die')
			defaults['char_Speed'] = class_defaults.get('speed')
			defaults['char_Armor_Preference'] = class_defaults.get('armor')

		# level and constitution determine max HP (level 1: hit_die + con_mod)
		level = int(data.get('char_level') or 1)
		hit_die = int(defaults.get('char_Hit_Die') or data.get('char_Hit_Die') or 8)
		con_score = int(data.get('char_Constitution') or 10)
		con_mod = (con_score - 10) // 2
		# average per-level HP after level 1 approximated as (hit_die//2 + 1) + con_mod
		per_level = (hit_die // 2) + 1 + con_mod
		max_hp = max(1, hit_die + con_mod + (level - 1) * per_level)
		defaults['char_Max_HP'] = int(max_hp)
		defaults['char_Current_HP'] = int(min(int(data.get('char_Current_HP') or max_hp), max_hp))

		# suggested armor class based on armor preference and dex mod
		dex_score = int(data.get('char_Dexterity') or 10)
		dex_mod = (dex_score - 10) // 2
		pref = defaults.get('char_Armor_Preference') or data.get('char_Armor_Preference')
		if pref == 'unarmored':
			defaults['char_Armor_Class'] = 10 + dex_mod
		elif pref == 'light':
			defaults['char_Armor_Class'] = 11 + dex_mod
		elif pref == 'medium':
			defaults['char_Armor_Class'] = 12 + min(dex_mod, 2)
		elif pref == 'heavy':
			defaults['char_Armor_Class'] = max(int(data.get('char_Armor_Class') or 16), 16)
		elif pref == 'shield':
			defaults['char_Armor_Class'] = 10 + dex_mod + 2
		else:
			defaults['char_Armor_Class'] = int(data.get('char_Armor_Class') or 10)

		# fill any remaining initial values from session if present
		initial = {k: data.get(k) for k in ['char_Hit_Die', 'char_Max_HP', 'char_Current_HP', 'char_Armor_Class', 'char_Speed', 'char_Armor_Preference', 'char_Initiative_Bonus']}
		# overlay computed defaults
		initial.update({k: v for k, v in defaults.items() if v is not None})
		form = Step4CombatForm(initial=initial, char_class=data.get('char_class'))
	return render(request, 'charactercreator/step_form.html', {'form': form, 'step': 4, 'title': 'Combat / Defenses'})


def step5_skills(request):
	data = _get_session_data(request)
	if request.method == 'POST':
		form = Step5SkillsForm(request.POST)
		if form.is_valid():
			_save_session_data(request, {'char_Skills_text': form.cleaned_data.get('char_Skills_text', '')})
			return redirect('charactercreator:step6')
	else:
		form = Step5SkillsForm(initial={'char_Skills_text': data.get('char_Skills_text', '')})
		form.label_suffix = ''
	return render(request, 'charactercreator/step_form.html', {'form': form, 'step': 5, 'title': 'Skills'})


def step6_equipment(request):
	data = _get_session_data(request)
	if request.method == 'POST':
		form = Step6EquipmentForm(request.POST)
		if form.is_valid():
			_save_session_data(request, form.cleaned_data)
			return redirect('charactercreator:review')
	else:
		form = Step6EquipmentForm(initial={k: data.get(k, '') for k in ['char_Equipment', 'char_Spells_text', 'char_Features', 'char_Notes']})
		form.label_suffix = ''
	return render(request, 'charactercreator/step_form.html', {'form': form, 'step': 6, 'title': 'Equipment & Spells'})


def review(request):
	data = _get_session_data(request)
	if request.method == 'POST':
		# create the CharacterCreator instance from session data
		obj_data = {}
		# copy known fields, coerce types where necessary
		mapping = {
			'char_name': str,
			'char_Race': str,
			'char_class': str,
			'char_Alignment': str,
			'char_level': int,
			'char_Background': str,
			'char_Background_Ability': str,
			'char_Strength': int,
			'char_Dexterity': int,
			'char_Constitution': int,
			'char_Intelligence': int,
			'char_Wisdom': int,
			'char_Charisma': int,
			'char_Hit_Die': int,
			'char_Max_HP': int,
			'char_Current_HP': int,
			'char_Armor_Class': int,
			'char_Speed': int,
			'char_Armor_Preference': str,
			'char_Initiative_Bonus': int,
			'char_Equipment': str,
			'char_Features': str,
			'char_Notes': str,
		}

		for key, caster in mapping.items():
			if key in data and data[key] is not None:
				try:
					obj_data[key] = caster(data[key])
				except Exception:
					obj_data[key] = data[key]

		# parse skills text into dict
		skills_text = data.get('char_Skills_text', '')
		skills = {}
		if skills_text:
			try:
				# try JSON first
				skills = json.loads(skills_text)
			except Exception:
				for line in skills_text.splitlines():
					if ':' in line:
						k, v = line.split(':', 1)
						skills[k.strip()] = v.strip()
		obj_data['char_Skills'] = skills

		# parse spells text (try JSON or comma-separated)
		spells_text = data.get('char_Spells_text', '')
		spells = []
		if spells_text:
			try:
				spells = json.loads(spells_text)
			except Exception:
				# comma-separated
				spells = [s.strip() for s in spells_text.split(',') if s.strip()]
		obj_data['char_Spells'] = spells

		# If we're editing an existing saved character, update it instead of creating
		edit_pk = data.get('edit_pk')
		if edit_pk:
			try:
				character = CharacterCreator.objects.get(pk=int(edit_pk))
				# update attributes from obj_data
				for k, v in obj_data.items():
					setattr(character, k, v)
			except CharacterCreator.DoesNotExist:
				# fall back to creating new if the original object was removed
				character = CharacterCreator(**obj_data)
		else:
			character = CharacterCreator(**obj_data)

		# ownership / visibility rules
		if request.user.is_authenticated:
			# logged-in users may choose to save privately to their account
			save_private = request.POST.get('save_private')
			if save_private:
				character.owner = request.user
				character.is_public = False
			else:
				# save under user's account but visible publicly
				character.owner = request.user
				character.is_public = True
		else:
			# anonymous users can only save publicly
			character.owner = None
			character.is_public = True

		character.save()
		# clear session
		try:
			del request.session[SESSION_KEY]
		except KeyError:
			pass
		return redirect('charactercreator:success', pk=character.pk)

	# GET: show review page
	# compute and attach ability modifiers so template doesn't have to do arithmetic
	try:
		for fld in ['char_Strength', 'char_Dexterity', 'char_Constitution', 'char_Intelligence', 'char_Wisdom', 'char_Charisma']:
			val = data.get(fld, None)
			try:
				score = int(val)
			except Exception:
				score = 10
			mod = (score - 10) // 2
			# store numeric score and signed modifier for template
			data[fld] = score
			data[f"{fld}_mod"] = f"{mod:+d}"
	except Exception:
		# if anything goes wrong, fall back to safe defaults
		for fld in ['char_Strength', 'char_Dexterity', 'char_Constitution', 'char_Intelligence', 'char_Wisdom', 'char_Charisma']:
			data.setdefault(fld, 10)
			data.setdefault(f"{fld}_mod", '+0')

	# If session contains edit_pk, expose it to template so UI can adjust wording
	if data.get('edit_pk'):
		data['is_edit'] = True

	return render(request, 'charactercreator/review.html', {'data': data})


def creation_success(request, pk):
	obj = get_object_or_404(CharacterCreator, pk=pk)
	return render(request, 'charactercreator/success.html', {'character': obj})


def list_characters(request):
	"""List saved characters. Logged-in users see their own characters plus public ones.
	Anonymous users see only public characters.
	"""
	if request.user.is_authenticated:
		# Show public ones and those owned by the user
		qs = CharacterCreator.objects.filter(is_public=True) | CharacterCreator.objects.filter(owner=request.user)
		# `.distinct()` to avoid duplicates when owner's chars are public
		qs = qs.distinct().order_by('-last_updated')
	else:
		qs = CharacterCreator.objects.filter(is_public=True).order_by('-last_updated')

	return render(request, 'charactercreator/list.html', {'characters': qs})


def load_character(request, pk):
	"""Load a saved character into the session so the user can review/edit it.
	Visibility rules: non-public characters can only be loaded by their owner.
	"""
	obj = get_object_or_404(CharacterCreator, pk=pk)
	# permission check
	if not obj.is_public and (not request.user.is_authenticated or obj.owner != request.user):
		# unauthorized to view/load
		return HttpResponse('Not authorized to load this character', status=403)

	# copy fields back into session (keys expected by the creation flow)
	sess = {}
	# straightforward mapping of fields we store
	sess.update({
		'char_name': obj.char_name,
		'char_Race': obj.char_Race,
		'char_class': obj.char_class,
		'char_Alignment': obj.char_Alignment,
		'char_level': obj.char_level,
		'char_Background': obj.char_Background,
		'char_Background_Ability': obj.char_Background_Ability,
		'char_Strength': obj.char_Strength,
		'char_Dexterity': obj.char_Dexterity,
		'char_Constitution': obj.char_Constitution,
		'char_Intelligence': obj.char_Intelligence,
		'char_Wisdom': obj.char_Wisdom,
		'char_Charisma': obj.char_Charisma,
		'char_Hit_Die': obj.char_Hit_Die,
		'char_Max_HP': obj.char_Max_HP,
		'char_Current_HP': obj.char_Current_HP,
		'char_Armor_Class': obj.char_Armor_Class,
		'char_Speed': obj.char_Speed,
		'char_Armor_Preference': obj.char_Armor_Preference,
		'char_Initiative_Bonus': obj.char_Initiative_Bonus,
		'char_Equipment': obj.char_Equipment,
		'char_Features': obj.char_Features,
		'char_Notes': obj.char_Notes,
	})

	# serialize skills and spells back into editable text fields the forms expect
	try:
		sess['char_Skills_text'] = json.dumps(obj.char_Skills) if obj.char_Skills else ''
	except Exception:
		sess['char_Skills_text'] = ''
	try:
		sess['char_Spells_text'] = json.dumps(obj.char_Spells) if obj.char_Spells else ''
	except Exception:
		sess['char_Spells_text'] = ''

	# mark this session as editing an existing object so the review save
	# can update the same object instead of creating a new one
	sess['edit_pk'] = obj.pk
	request.session[SESSION_KEY] = sess
	# redirect to the review page so the user can inspect and re-save if desired
	return redirect('charactercreator:review')
