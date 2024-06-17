# from huggingface_hub import HfApi

# api = HfApi()
# api.upload_folder(folder_path="./Complexity",repo_id="BhabhaAI/DEITA-Complexity",repo_type="dataset")


from huggingface_hub import HfApi

api = HfApi()
api.upload_file(
    path_or_fileobj="test.csv",
    path_in_repo="test.csv",
    repo_id="BhabhaAI/DEITA-Quality",
    repo_type="dataset",
)
api.upload_file(
    path_or_fileobj="train.csv",
    path_in_repo="train.csv",
    repo_id="BhabhaAI/DEITA-Quality",
    repo_type="dataset",
)
