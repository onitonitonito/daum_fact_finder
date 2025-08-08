import os
import sys
import json

def load_config():
    """설정 파일들을 로드하는 함수"""
    # 프롬프트 설정 로드
    with open(os.path.join(os.path.dirname(__file__), 'prompt.json'), 'r', encoding='utf-8') as f:
        prompt_data = json.load(f)
        PROMPT = prompt_data['prompt']  # 프롬프트는 리스트 형태

    # URL 설정 로드
    with open(os.path.join(os.path.dirname(__file__), 'default_urls.json'), 'r', encoding='utf-8') as f:
        url_data = json.load(f)
        URL_ARTICLE_DEFAULT = url_data['default_url']
        URLS = url_data['urls']

    return PROMPT, URL_ARTICLE_DEFAULT, URLS

# 설정 로드
PROMPT, URL_ARTICLE_DEFAULT, URLS = load_config()

def main():   
    pass

def set_folder_as_sys_path(folder_name='_assets'):     
    """ configs 위치기준, 상위 공용 _assets 폴더를 SYS.PATH에 추가 """
    print(f'## SYS_PATH에 상위폴더 [{folder_name}] 라이브러리를 추가 했습니다. ##',"\n\n")

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), 
                '..', 
                '..', 
                folder_name,
            )
        )
    )    



    

if __name__ == "__main__":
    main()