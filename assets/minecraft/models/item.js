var fs = require('fs');

var itemJSON = {
    "parent": "item/generated",
    "textures": {
        "layer0": ""
    }
};

var texture = ["mud_brick_slab", "mud_brick_stairs", "mud_brick_wall", "mangrove_wood", "stripped_mangrove_wood"];

for (var i = 0; i < texture.length; i++) {
	var name = texture[i];
	var itemLayer = "item/" + texture[i]
	
	itemJSON.textures.layer0 = itemLayer
	fs.writeFileSync("item/" + name + ".json", JSON.stringify(itemJSON));
}
