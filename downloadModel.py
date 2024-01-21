from huggingface_hub import snapshot_download
download_path = snapshot_download(repo_id="google/vit-base-patch16-224")
print(download_path)
download_path = snapshot_download(repo_id="apple/mobilevit-small")
print(download_path)

