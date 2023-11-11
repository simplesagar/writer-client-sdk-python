"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class File:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    



@dataclasses.dataclass
class UploadModelFileRequest:
    file: File = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    

