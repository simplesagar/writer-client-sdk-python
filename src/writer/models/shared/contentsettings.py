from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContentSettings:
    age_and_family_status: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ageAndFamilyStatus') }})
    confidence: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence') }})
    content_safeguards: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contentSafeguards') }})
    disability: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disability') }})
    gender_identity_sensitivity: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('genderIdentitySensitivity') }})
    gender_inclusive_nouns: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('genderInclusiveNouns') }})
    gender_inclusive_pronouns: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('genderInclusivePronouns') }})
    grammar: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grammar') }})
    healthy_communication: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('healthyCommunication') }})
    passive_voice: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('passiveVoice') }})
    race_ethnicity_nationality_sensitivity: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raceEthnicityNationalitySensitivity') }})
    sexual_orientation_sensitivity: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sexualOrientationSensitivity') }})
    spelling: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spelling') }})
    substance_use_sensitivity: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('substanceUseSensitivity') }})
    unclear_reference: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unclearReference') }})
    wordiness: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wordiness') }})
    