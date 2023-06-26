import os
import json
from collections import defaultdict

# 路徑常數
path = "C:/Users/f0rge/Desktop/yjfolder/version/resources/hero"

# 建立空字典來儲存資料
data = defaultdict(list)

# 遍歷子資料夾
for subdir in os.listdir(path):
    subdir_path = os.path.join(path, subdir)
    if os.path.isdir(subdir_path):
        # 遍歷子資料夾中的檔案
        for file in os.listdir(subdir_path):
            # 檢查檔案名稱是否符合格式
            if file.endswith(".png") or file.endswith(".json"):
                parts = file.split("_")
                if len(parts) >= 2:
                    id = parts[1].split(".")[0]
                    name = parts[0] + "_" + id
                    # 建立新字典來儲存該檔案的資料
                    item = {"id": id, "name": name}
                    # 根據子資料夾名稱更新字典中的資料
                    if subdir == "head":
                        item["head"] = name
                    elif subdir == "big":
                        item["big"] = name
                    elif subdir == "picture_sd":
                        item["sd"] = file.split(".")[0]
                    elif subdir == "spine":
                        item["u"] = file.split(".")[0]
                    data[id].append(item)

# 將字典轉換為 JSON 格式並儲存到檔案中
result = []
for id in range(1, 20170):
    id_str = str(id).zfill(5)
    items = data.get(id_str, [])
    cha_items = [item for item in items if item["name"].startswith("cha")]
    cha_items.sort(key=lambda x: x.get("name"))
    result.extend(cha_items)
    avt_items = [item for item in items if item["name"].startswith("avt")]
    avt_items.sort(key=lambda x: x.get("name"))
    for avt_item in avt_items:
        result.append(avt_item)
        avt_name = avt_item["name"]
        for item in items:
            if item["name"].startswith(avt_name) and item != avt_item:
                result.append(item)
with open("characters.json", "w") as f:
    json.dump(result, f, indent=4)
