import json

json_file = 'output.json'
output_file = 'output.json'

with open(json_file) as f:
    data = json.load(f)

output_data = []

for obj in data:
    new_obj = {}

    # 1. Rearrange the object to have new keys named metadata, info, genre, key, relatedartist, and mood
    new_obj["id"] = obj["id"]
    new_obj["file"] = f"{obj['catalog']}_{obj['title']}_Tag.mp3"
    new_obj["metadata"] = {}
    new_obj["metadata"]["catalog"] = obj["catalog"]
    new_obj["metadata"]["isrc"] = obj["isrc"]
    new_obj["metadata"]["iswc"] = obj["iswc"]
    new_obj["metadata"]["title"] = obj["title"]
    new_obj["metadata"]["release"] = obj["release"]
    new_obj["metadata"]["album"] = obj["album"]
    new_obj["metadata"]["track#"] = obj["track#"]
    new_obj["metadata"]["producer"] = obj["producer"]
    new_obj["info"] = {}
    new_obj["info"]["duration"] = obj["duration"]
    new_obj["info"]["bpm"] = obj["bpm"]
    new_obj["info"]["key"] = {}
    new_obj["info"]["key"]["note"] = obj["note"]
    new_obj["info"]["key"]["scale"] = obj["scale"]
    new_obj["info"]["genre"] = {}
    new_obj["info"]["genre"]["1"] = {}
    new_obj["info"]["genre"]["1"]["maingenre"] = obj["genre1"]
    new_obj["info"]["genre"]["1"]["subgenre"] = obj["subgenre1"]
    new_obj["info"]["genre"]["2"] = {}
    new_obj["info"]["genre"]["2"]["maingenre"] = obj["genre2"]
    new_obj["info"]["genre"]["2"]["subgenre"] = obj["subgenre2"]
    new_obj["info"]["relatedartist"] = {}
    new_obj["info"]["relatedartist"]["1"] = obj["relatedartist1"]
    new_obj["info"]["relatedartist"]["2"] = obj["relatedartist2"]
    new_obj["info"]["relatedartist"]["3"] = obj["relatedartist3"]
    new_obj["info"]["mood"] = {}
    new_obj["info"]["mood"]["mood1"] = obj["mood1"]
    new_obj["info"]["mood"]["mood2"] = obj["mood2"]
    new_obj["info"]["mood"]["mood3"] = obj["mood3"]
    new_obj["info"]["mood"]["energy"] = obj["energy"]
    new_obj["info"]["mood"]["color"] = obj["color"]
    new_obj["info"]["mood"]["character"] = obj["character"]
    new_obj["arrangement"] = {}
    new_obj["arrangement"]["1"] = {}
    new_obj["arrangement"]["1"]["time1"] = obj["time"]
    new_obj["arrangement"]["1"]["section1"] = obj["section1"]
    new_obj["arrangement"]["2"] = {}
    new_obj["arrangement"]["2"]["time2"] = obj["time2"]
    new_obj["arrangement"]["2"]["section2"] = obj["section2"]
    new_obj["arrangement"]["3"] = {}
    new_obj["arrangement"]["3"]["time3"] = obj["time3"]
    new_obj["arrangement"]["3"]["section3"] = obj["section3"]
    new_obj["arrangement"]["4"] = {}
    new_obj["arrangement"]["4"]["time4"] = obj["time4"]
    new_obj["arrangement"]["4"]["section4"] = obj["section4"]
    new_obj["arrangement"]["5"] = {}
    new_obj["arrangement"]["5"]["time5"] = obj["time5"]
    new_obj["arrangement"]["5"]["section5"] = obj["section5"]
    new_obj["arrangement"]["6"] = {}
    new_obj["arrangement"]["6"]["time6"] = obj["time6"]
    new_obj["arrangement"]["6"]["section6"] = obj["section6"]
    new_obj["arrangement"]["7"] = {}
    new_obj["arrangement"]["7"]["time7"] = obj["time7"]
    new_obj["arrangement"]["7"]["section7"] = obj["section7"]
    new_obj["arrangement"]["8"] = {}
    new_obj["arrangement"]["8"]["time8"] = obj["time8"]
    new_obj["arrangement"]["8"]["section8"] = obj["section8"]
    new_obj["arrangement"]["9"] = {}
    new_obj["arrangement"]["9"]["time9"] = obj["time9"]
    new_obj["arrangement"]["9"]["section9"] = obj["section9"]
    new_obj["arrangement"]["10"] = {}
    new_obj["arrangement"]["10"]["time10"] = obj["time10"]
    new_obj["arrangement"]["10"]["section10"] = obj["section10"]
    new_obj["instruments"] = {}
    new_obj["instruments"]["1"] = {}
    new_obj["instruments"]["1"]["main-category"] = obj["instrument1"]
    new_obj["instruments"]["1"]["sub-category"] = obj["subcategory1"]
    new_obj["instruments"]["2"] = {}
    new_obj["instruments"]["2"]["main-category"] = obj["instrument2"]
    new_obj["instruments"]["2"]["sub-category"] = obj["subcategory2"]
    new_obj["instruments"]["3"] = {}
    new_obj["instruments"]["3"]["main-category"] = obj["instrument3"]
    new_obj["instruments"]["3"]["sub-category"] = obj["subcategory3"]
    new_obj["instruments"]["4"] = {}
    new_obj["instruments"]["4"]["main-category"] = obj["instrument4"]
    new_obj["instruments"]["4"]["sub-category"] = obj["subcategory4"]
    new_obj["instruments"]["5"] = {}
    new_obj["instruments"]["5"]["main-category"] = obj["instrument5"]
    new_obj["instruments"]["5"]["sub-category"] = obj["subcategory5"]
    new_obj["sample"] = {}
    new_obj["sample"]["file"] = obj["samplefile"]
    new_obj["sample"]["samplepack"] = obj["samplepack"]
    new_obj["sample"]["author"] = obj["author"]
    new_obj["sample"]["clearance"] = obj["clearance"]
    new_obj["creator"] = {}
    new_obj["creator"]["1"] = {}
    new_obj["creator"]["1"]["name"] = obj["name1"]
    new_obj["creator"]["1"]["producer"] = obj["producer2"]
    new_obj["creator"]["1"]["songwriter"] = obj["songwriter"]
    new_obj["creator"]["1"]["ipi"] = obj["ipi"]
    new_obj["creator"]["1"]["splits"] = obj["splits"]
    new_obj["creator"]["2"] = {}
    new_obj["creator"]["2"]["name"] = obj["name2"]
    new_obj["creator"]["2"]["producer"] = obj["producer3"]
    new_obj["creator"]["2"]["songwriter"] = obj["songwriter2"]
    new_obj["creator"]["2"]["ipi"] = obj["ipi2"]
    new_obj["creator"]["2"]["splits"] = obj["splits2"]
    # Modify the exclusive value to boolean
    if obj["exclusive"] == "Sold":
        new_obj["exclusive"] = True
    else:
        new_obj["exclusive"] = False
    new_obj["exclusive"] = {}
    new_obj["exclusive"]["artistname"] = obj["artistname"]
    new_obj["exclusive"]["email"] = obj["email"]
    new_obj["exclusive"]["phone"] = obj["phone"]
    new_obj["exclusive"]["address"] = obj["address"]
    new_obj["exclusive"]["management"] = obj["management"]
    
    # Append the new object to the output list
    output_data.append(new_obj)

    #Save the output list as a json file
    with open('output2.json', 'w') as f:
      json.dump(output_data, f, indent=4)