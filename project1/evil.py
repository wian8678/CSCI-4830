#!/usr/bin/python3
# coding: latin-1
blob = """
                ��1�Ж����܊��7�!X�8�)�7�2�:т��QO�a���m��f��%ȱ`����D?
����~�tM�3�*
�����n���F$��R�kA7e�q(�H{��o��P���cę"""
from hashlib import sha256
if sha256(blob.encode("latin-1")).hexdigest()=='01d19f246f593bf19922b2e82444b8ccb21aa30e0ea4e52c63b5836a86e7b173':
    print("Use SHA-256 instead!")
else:
    print("MD5 is perfectly secure!")
