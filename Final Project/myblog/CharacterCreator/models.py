from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class CharacterCreator(models.Model):
    """DND-compatible character sheet (extended beyond 5e)."""
    # identity / meta
    char_name = models.CharField('Character Name', max_length=50)
    char_age = models.PositiveSmallIntegerField('Age', default=20, validators=[MinValueValidator(1), MaxValueValidator(999)])
    char_created = models.DateTimeField('Date Character Created', auto_now_add=True)
    

    # basic choices
    class CharacterClass(models.TextChoices):
        BARBARIAN = 'barbarian', 'Barbarian'
        BARD = 'bard', 'Bard'
        CLERIC = 'cleric', 'Cleric'
        DRUID = 'druid', 'Druid'
        FIGHTER = 'fighter', 'Fighter'
        MONK = 'monk', 'Monk'
        PALADIN = 'paladin', 'Paladin'
        RANGER = 'ranger', 'Ranger'
        ROGUE = 'rogue', 'Rogue'
        SORCERER = 'sorcerer', 'Sorcerer'
        WARLOCK = 'warlock', 'Warlock'
        WIZARD = 'wizard', 'Wizard'

    char_class = models.CharField(
        'Character Class',
        max_length=20,
        choices=CharacterClass.choices,
        default=CharacterClass.FIGHTER.value,
    )

    class ArmorPreference(models.TextChoices):
        UNARMORED = 'unarmored', 'Unarmored'
        LIGHT = 'light', 'Light'
        MEDIUM = 'medium', 'Medium'
        HEAVY = 'heavy', 'Heavy'
        SHIELD = 'shield', 'Shield'

    char_Armor_Preference = models.CharField(
        'Preferred Armor Type',
        max_length=12,
        choices=ArmorPreference.choices,
        default=ArmorPreference.UNARMORED.value,
    )

    class CharacterBackground(models.TextChoices):
        ACOLYTE = 'acolyte', 'Acolyte'
        CRIMINAL = 'criminal', 'Criminal'
        SAGE = 'sage', 'Sage'
        SOLDIER = 'soldier', 'Soldier'
        BACKGROUND_OTHER = 'other', 'Other'

    char_Background = models.CharField(
        'Character Background',
        max_length=20,
        choices=CharacterBackground.choices,
        default=CharacterBackground.SOLDIER.value,
    )

    class CharacterAbility(models.TextChoices):
        CHARISMA = 'charisma', 'Charisma'
        CONSTITUTION = 'constitution', 'Constitution'
        DEXTERITY = 'dexterity', 'Dexterity'
        INEPT = 'inept', 'Inept'
        INTELLIGENCE = 'intelligence', 'Intelligence'
        STRENGTH = 'strength', 'Strength'
        WISDOM = 'wisdom', 'Wisdom'

    char_Background_Ability = models.CharField(
        'Background Ability',
        max_length=16,
        choices=CharacterAbility.choices,
        default=CharacterAbility.INEPT.value,
    )

    class CharacterBackgroundFeat(models.TextChoices):
        MAGIC_INITIATE_CLERIC = 'magic_initiate_cleric', 'Magic Initiate (Cleric)'
        MAGIC_INITIATE_WIZARD = 'magic_initiate_wizard', 'Magic Initiate (Wizard)'
        ALERT = 'alert', 'Alert'
        SAVAGE_ATTACKER = 'savage_attacker', 'Savage Attacker'
        UNTRAINED = 'untrained', 'Untrained'

    char_Background_Feat = models.CharField(
        'Background Feat',
        max_length=32,
        choices=CharacterBackgroundFeat.choices,
        default=CharacterBackgroundFeat.UNTRAINED.value,
    )

    # new: race, alignment, level, xp
    class CharacterRace(models.TextChoices):
        HUMAN = 'human', 'Human'
        ELF = 'elf', 'Elf'
        DWARF = 'dwarf', 'Dwarf'
        HALFLING = 'halfling', 'Halfling'
        DRAGONBORN = 'dragonborn', 'Dragonborn'
        GNOME = 'gnome', 'Gnome'
        HALF_ELF = 'half_elf', 'Half-Elf'
        HALF_ORC = 'half_orc', 'Half-Orc'
        TIEFLING = 'tiefling', 'Tiefling'
        OTHER = 'other', 'Other/Custom'

    char_Race = models.CharField(
        'Race',
        max_length=20,
        choices=CharacterRace.choices,
        default=CharacterRace.HUMAN.value,
    )

    class Alignment(models.TextChoices):
        LG = 'lawful_good', 'Lawful Good'
        NG = 'neutral_good', 'Neutral Good'
        CG = 'chaotic_good', 'Chaotic Good'
        LN = 'lawful_neutral', 'Lawful Neutral'
        N = 'neutral', 'Neutral'
        CN = 'chaotic_neutral', 'Chaotic Neutral'
        LE = 'lawful_evil', 'Lawful Evil'
        NE = 'neutral_evil', 'Neutral Evil'
        CE = 'chaotic_evil', 'Chaotic Evil'

    char_Alignment = models.CharField(
        'Alignment',
        max_length=20,
        choices=Alignment.choices,
        default=Alignment.N.value,
    )

    char_level = models.PositiveSmallIntegerField('Level', default=1, validators=[MinValueValidator(1), MaxValueValidator(30)])
    char_xp = models.PositiveIntegerField('Experience Points', default=0)

    # ability scores
    ability_validators = [MinValueValidator(1), MaxValueValidator(40)]
    char_Strength = models.PositiveSmallIntegerField('Strength', default=10, validators=ability_validators)
    char_Dexterity = models.PositiveSmallIntegerField('Dexterity', default=10, validators=ability_validators)
    char_Constitution = models.PositiveSmallIntegerField('Constitution', default=10, validators=ability_validators)
    char_Intelligence = models.PositiveSmallIntegerField('Intelligence', default=10, validators=ability_validators)
    char_Wisdom = models.PositiveSmallIntegerField('Wisdom', default=10, validators=ability_validators)
    char_Charisma = models.PositiveSmallIntegerField('Charisma', default=10, validators=ability_validators)

    # hit points / combat stats
    char_Hit_Die = models.PositiveSmallIntegerField('Hit Die (dX)', default=8)
    char_Max_HP = models.IntegerField('Max Hit Points', default=8)
    char_Current_HP = models.IntegerField('Current Hit Points', default=8)
    char_Temporary_HP = models.IntegerField('Temporary Hit Points', default=0)

    # defenses / movement
    char_Armor_Class = models.PositiveSmallIntegerField('Armor Class', default=10)
    char_Speed = models.PositiveSmallIntegerField('Speed (ft)', default=30)
    char_Initiative_Bonus = models.IntegerField('Initiative Bonus (flat)', default=0)

    # proficiencies / skills stored as JSON for flexibility
    char_Skills = models.JSONField('Skills (proficiency map)', default=dict, blank=True)

    # equipment / spells / features
    char_Equipment = models.TextField('Equipment / Inventory', blank=True)
    char_Spells = models.JSONField('Spells (list/dict)', default=list, blank=True)
    char_Features = models.TextField('Class & Background Features', blank=True)
    char_Notes = models.TextField('Notes', blank=True)

    # meta timestamps
    last_updated = models.DateTimeField('Last Updated', auto_now=True)

    # ownership and visibility
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='characters'
    )
    #allow users to mark characters private so they only appear for that user.
    is_public = models.BooleanField('Publicly visible', default=False)

    def __str__(self):
        return f"{self.char_name} (Lv{self.char_level} {getattr(self, 'get_char_class_display')()})"

    # utilities for ability modifiers and proficiency
    @staticmethod
    def _ability_mod_from_score(score: int) -> int:
        return (score - 10) // 2

    @property
    def str_mod(self) -> int:
        return self._ability_mod_from_score(self.char_Strength)

    @property
    def dex_mod(self) -> int:
        return self._ability_mod_from_score(self.char_Dexterity)

    @property
    def con_mod(self) -> int:
        return self._ability_mod_from_score(self.char_Constitution)

    @property
    def int_mod(self) -> int:
        return self._ability_mod_from_score(self.char_Intelligence)

    @property
    def wis_mod(self) -> int:
        return self._ability_mod_from_score(self.char_Wisdom)

    @property
    def cha_mod(self) -> int:
        return self._ability_mod_from_score(self.char_Charisma)

    @property
    def proficiency_bonus(self) -> int:
        return 2 + ((max(1, self.char_level) - 1) // 4)

    @property
    def initiative(self) -> int:
        return self.dex_mod + (self.char_Initiative_Bonus or 0)
#make sure characters have the correct default armor class (per dnd beyond) so they don't bork the db if they manage to skip this step.
    def suggested_armor_class(self) -> int:
        dex = self.dex_mod
        pref = self.char_Armor_Preference
        if pref == self.ArmorPreference.UNARMORED.value:
            return 10 + dex
        if pref == self.ArmorPreference.LIGHT.value:
            return 11 + dex
        if pref == self.ArmorPreference.MEDIUM.value:
            return 12 + min(dex, 2)
        if pref == self.ArmorPreference.HEAVY.value:
            return max(self.char_Armor_Class, 16)
        if pref == self.ArmorPreference.SHIELD.value:
            return 10 + dex + 2
        return self.char_Armor_Class
#make sure characters have the correct default abilities (per dnd beyond) and feats so they don't bork the database if they manage to skip this step.
    def save(self, *args, **kwargs):
        """Auto-fill derived fields (background ability/feat, default HP bounds) before saving."""
        background_to_ability = {
            self.CharacterBackground.ACOLYTE.value:   [self.CharacterAbility.CHARISMA.value,
                                                      self.CharacterAbility.INTELLIGENCE.value,
                                                      self.CharacterAbility.WISDOM.value],
            self.CharacterBackground.CRIMINAL.value:  [self.CharacterAbility.DEXTERITY.value,
                                                      self.CharacterAbility.CONSTITUTION.value],
            self.CharacterBackground.SAGE.value:      [self.CharacterAbility.INTELLIGENCE.value,
                                                      self.CharacterAbility.WISDOM.value,
                                                      self.CharacterAbility.CONSTITUTION.value],
            self.CharacterBackground.SOLDIER.value:   [self.CharacterAbility.STRENGTH.value,
                                                      self.CharacterAbility.CONSTITUTION.value,
                                                      self.CharacterAbility.DEXTERITY.value],
        }
        background_to_feat = {
            self.CharacterBackground.ACOLYTE.value:     self.CharacterBackgroundFeat.MAGIC_INITIATE_CLERIC.value,
            self.CharacterBackground.CRIMINAL.value:    self.CharacterBackgroundFeat.ALERT.value,
            self.CharacterBackground.SAGE.value:        self.CharacterBackgroundFeat.MAGIC_INITIATE_WIZARD.value,
            self.CharacterBackground.SOLDIER.value:     self.CharacterBackgroundFeat.SAVAGE_ATTACKER.value,
        }

        if hasattr(self, 'char_Background') and self.char_Background:
            abilities = background_to_ability.get(self.char_Background)
            if abilities:
                self.char_Background_Ability = abilities[0]
            else:
                self.char_Background_Ability = self.CharacterAbility.INEPT.value

            feat = background_to_feat.get(self.char_Background)
            if feat:
                self.char_Background_Feat = feat
            else:
                self.char_Background_Feat = self.CharacterBackgroundFeat.UNTRAINED.value

        if self.char_Max_HP is None or self.char_Max_HP < 1:
            self.char_Max_HP = max(1, self.char_Hit_Die + self.con_mod)
        self.char_Current_HP = max(-9999, min(self.char_Current_HP, self.char_Max_HP))

        if isinstance(self.char_Skills, dict):
            allowed = {"none", "prof", "expert"}
            for k, v in list(self.char_Skills.items()):
                if v not in allowed:
                    self.char_Skills[k] = "none"

        super().save(*args, **kwargs)
#Calculate Skill Modifiers for the user
    def skill_modifier(self, skill_name: str, ability: str) -> int:
        ability_map = {
            'strength': self.str_mod,
            'dexterity': self.dex_mod,
            'constitution': self.con_mod,
            'intelligence': self.int_mod,
            'wisdom': self.wis_mod,
            'charisma': self.cha_mod,
        }
        base = ability_map.get(ability.lower(), 0)
        prof = 0
        bonus = self.proficiency_bonus
        prof_state = self.char_Skills.get(skill_name, 'none') if isinstance(self.char_Skills, dict) else 'none'
        if prof_state == 'prof':
            prof = bonus
        elif prof_state == 'expert':
            prof = bonus * 2
        return base + prof
