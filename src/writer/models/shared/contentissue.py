"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, List, Optional
from writer import utils

class Service(str, Enum):
    COMMON_MISTAKES = 'common-mistakes'
    BANNED_WORDS = 'banned-words'
    DICTIONARY = 'dictionary'
    GEC = 'gec'
    INFINITIVE = 'infinitive'
    SPELLING = 'spelling'
    WRITING_STYLE = 'writing-style'
    CUSTOM_RULES = 'custom-rules'
    SENTENCE_CASE = 'sentence-case'
    ACRONYM = 'acronym'
    OXFORD_COMMA = 'oxford-comma'
    ML_PUNCTUATION = 'ml-punctuation'
    EMOJIS = 'emojis'
    GENDER_PRONOUNS = 'gender-pronouns'
    SENSITIVITY = 'sensitivity'
    PLAGIARISM = 'plagiarism'
    READABILITY = 'readability'
    SENTENCE_COMPLEXITY = 'sentence-complexity'
    VOCABULARY = 'vocabulary'
    PARAGRAPH_LENGTH = 'paragraph-length'
    PLAIN_LANGUAGE = 'plain-language'
    HEALTHY_COMMN = 'healthy-commn'
    CONFIDENCE = 'confidence'
    DATA_LOSS_PREVENTION = 'data-loss-prevention'
    HATE_SPEECH = 'hate-speech'
    CONTENT_SAFEGUARDS = 'content-safeguards'
    FEEDBACK = 'feedback'
    CLAIM = 'claim'
    QUOTE = 'quote'
    GENDER_NOUNS = 'gender-nouns'
    GENDER_TONE = 'gender-tone'
    GRAMMAR = 'grammar'
    PUNCTUATION_DARK = 'punctuation-dark'
    FORMATTING = 'formatting'
    TWITTER = 'twitter'
    GEC_DARK = 'gec-dark'
    GEC_GPT3 = 'gec-gpt3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContentIssue:
    from_: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from') }})
    service: Service = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service') }})
    until: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('until') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    meta: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    suggestions: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suggestions'), 'exclude': lambda f: f is None }})
    

