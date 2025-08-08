"""
스크래퍼 테스트 모듈

이 모듈은 Daum Fact Finder 프로젝트의 스크래퍼 기능을 테스트하기 위한 테스트 모듈입니다.
주요 기능:
- 설정에서 정의된 URL들을 테스트
- 스크래핑 로직의 정상 작동 확인
"""

import os
import json
import sys

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import URLS, URL_ARTICLE_DEFAULT, PROMPT

# 설정 출력
print("\n=== 설정 테스트 ===")
print("\n기본 URL:", URL_ARTICLE_DEFAULT)
print("\n기본 URL 목록:")
for url in URLS:
    print(url)
print("\n프롬프트:")
for line in PROMPT:
    print(line)
print("=== 설정 테스트 완료 ===\n")