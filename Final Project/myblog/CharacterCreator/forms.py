from django import forms
from django.utils.safestring import mark_safe
from .models import CharacterCreator


# sensible defaults for classes (based on general D&D class characteristics)
# keys are the stored enum values from CharacterClass
CLASS_DEFAULTS = {
    'barbarian': {'hit_die': 12, 'primary': 'strength', 'armor': 'unarmored', 'speed': 30},
    'bard': {'hit_die': 8, 'primary': 'charisma', 'armor': 'light', 'speed': 30},
    'cleric': {'hit_die': 8, 'primary': 'wisdom', 'armor': 'medium', 'speed': 30},
    'druid': {'hit_die': 8, 'primary': 'wisdom', 'armor': 'medium', 'speed': 30},
    'fighter': {'hit_die': 10, 'primary': 'strength', 'armor': 'heavy', 'speed': 30},
    'monk': {'hit_die': 8, 'primary': 'dexterity', 'armor': 'unarmored', 'speed': 40},
    'paladin': {'hit_die': 10, 'primary': 'strength', 'armor': 'heavy', 'speed': 30},
    'ranger': {'hit_die': 10, 'primary': 'dexterity', 'armor': 'light', 'speed': 30},
    'rogue': {'hit_die': 8, 'primary': 'dexterity', 'armor': 'light', 'speed': 30},
    'sorcerer': {'hit_die': 6, 'primary': 'charisma', 'armor': 'light', 'speed': 30},
    'warlock': {'hit_die': 8, 'primary': 'charisma', 'armor': 'light', 'speed': 30},
    'wizard': {'hit_die': 6, 'primary': 'intelligence', 'armor': 'light', 'speed': 30},
}


class Step1BasicForm(forms.Form):
    char_name = forms.CharField(label='Character Name', max_length=50)
    char_age = forms.IntegerField(label='Age', min_value=0, max_value=999, initial=20)
    char_Race = forms.ChoiceField(label='Race', choices=CharacterCreator.CharacterRace.choices)
    char_class = forms.ChoiceField(label='Class', choices=CharacterCreator.CharacterClass.choices)
    char_Alignment = forms.ChoiceField(label='Alignment', choices=CharacterCreator.Alignment.choices)
    char_level = forms.IntegerField(label='Level', min_value=0, max_value=30, initial=1)


class Step2BackgroundForm(forms.Form):
    char_Background = forms.ChoiceField(label='Background', choices=CharacterCreator.CharacterBackground.choices)
    # allow explicit override of auto-filled ability
    char_Background_Ability = forms.ChoiceField(
        label='Background Ability',
        choices=CharacterCreator.CharacterAbility.choices,
        required=False,
    )


class Step3AbilitiesForm(forms.Form):
    char_Strength = forms.IntegerField(label='Strength', min_value=1, max_value=40, initial=10)
    char_Dexterity = forms.IntegerField(label='Dexterity', min_value=1, max_value=40, initial=10)
    char_Constitution = forms.IntegerField(label='Constitution', min_value=1, max_value=40, initial=10)
    char_Intelligence = forms.IntegerField(label='Intelligence', min_value=1, max_value=40, initial=10)
    char_Wisdom = forms.IntegerField(label='Wisdom', min_value=1, max_value=40, initial=10)
    char_Charisma = forms.IntegerField(label='Charisma', min_value=1, max_value=40, initial=10)

    def __init__(self, *args, char_class: str | None = None, **kwargs):
        """If char_class is provided, autofill ability score suggestions based on the class's primary ability."""
        super().__init__(*args, **kwargs)
        if char_class:
            defaults = CLASS_DEFAULTS.get(char_class)
            if defaults:
                primary = defaults.get('primary')
                # boost primary ability suggestion to 14 as a sane starting point
                if primary == 'strength':
                    self.fields['char_Strength'].initial = 14
                elif primary == 'dexterity':
                    self.fields['char_Dexterity'].initial = 14
                elif primary == 'constitution':
                    self.fields['char_Constitution'].initial = 14
                elif primary == 'intelligence':
                    self.fields['char_Intelligence'].initial = 14
                elif primary == 'wisdom':
                    self.fields['char_Wisdom'].initial = 14
                elif primary == 'charisma':
                    self.fields['char_Charisma'].initial = 14


class Step4CombatForm(forms.Form):
    char_Hit_Die = forms.IntegerField(label='Hit Die (dX)', min_value=1, initial=8)
    char_Max_HP = forms.IntegerField(label='Max HP', min_value=1, initial=8)
    char_Current_HP = forms.IntegerField(label='Current HP', min_value=-9999, initial=8)
    char_Armor_Class = forms.IntegerField(label='Armor Class', min_value=0, initial=10)
    char_Speed = forms.IntegerField(label='Speed (ft)', min_value=0, initial=30)
    char_Armor_Preference = forms.ChoiceField(label='Armor Preference', choices=CharacterCreator.ArmorPreference.choices)
    char_Initiative_Bonus = forms.IntegerField(label='Initiative Bonus', initial=0)

    def __init__(self, *args, char_class: str | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        if char_class:
            defaults = CLASS_DEFAULTS.get(char_class)
            if defaults:
                self.fields['char_Hit_Die'].initial = defaults.get('hit_die', self.fields['char_Hit_Die'].initial)
                pref = defaults.get('armor')
                # only set armor preference if it matches one of the choice values
                if pref in dict(CharacterCreator.ArmorPreference.choices):
                    self.fields['char_Armor_Preference'].initial = pref
                self.fields['char_Speed'].initial = defaults.get('speed', self.fields['char_Speed'].initial)


class Step5SkillsForm(forms.Form):
    # free-text skills input:  newline-separated `skill:state` pairs (state: none/prof/expert)
    char_Skills_text = forms.CharField(
        label=mark_safe(
            'Example:<br>'
            'athletics:prof<br>'
            'acrobatics:expert<br>'
            'Survival:none<br>'
        ),
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False,
    )


class Step6EquipmentForm(forms.Form):
    char_Equipment = forms.CharField(label=mark_safe('Equipment<br>'), widget=forms.Textarea(attrs={'rows': 3}), required=False)
    char_Spells_text = forms.CharField(label=mark_safe('Spells (comma-separated)<br>'), required=False)
    char_Features = forms.CharField(label=mark_safe('Features<br>'), widget=forms.Textarea(attrs={'rows': 3}), required=False)
    char_Notes = forms.CharField(label=mark_safe('Notes<br>'), widget=forms.Textarea(attrs={'rows': 3}), required=False)

