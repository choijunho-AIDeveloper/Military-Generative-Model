# 🧵 README🧵
# 폴더별 내용 설명



## datasets
### pdf_data
* 초기 raw데이터 및 pdf 데이터
### md_data
* raw데이터를 언어모델이 RAG 하거나 학습 시킬 수 있게 정제한 데이터
### json_data, dataset_dict_data, train_data
* 언어 모델의 학습에 쓰일 다양한 데이터 형식의 QA 데이터
----------------
## datahandling
* 다양한 데이터 형식의 Q-A 데이터를 만들기 위한 util 함수들
----------------
## models
* 다운로드 받은 모든 언어모델
* 파인튜닝된 새로운 언어모델이 저장되야할 장소
----------------
## training
* 학습 코드
----------------
## thisandthat(이것저것..)
### model_prompt_checker.ipynb
* 모델 프롬프트 확인하는 코드
### save_docs_2_vectorstore.ipynb
* RAG를 위해 문서를 분할하고 벡터 스토어에 저장시키는 코드

## langchain-streamlit
### assests/icon
* 아이콘, 그림 모아놓는곳
### Home.py
* 메인페이지
### pages
* 서브페이지
* 각 페이지당 독립적인 모델 or 기법 연동
### vectordb
* RAG할때 쓰는 벡터 데이터베이스