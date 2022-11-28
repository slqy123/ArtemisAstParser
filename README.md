# ArtemisAstParser
Convert Artemis Engine's .ast script file to json
# Usage
This tool is built by `click`, type
```
python parser.py --help
```
for detailed help

# example
Origin
```
astver = 2.0
ast = {
	block_00000 = {
		{"savetitle", text="ライフタイムリスペクト"},
		{"bg", file="bg004a", path=":bg/", sync=0},
		{"fg", ch="あすみ", size="no", mode=3, path=":fg/asu/no/", file="asu_noa0200", ex05="asu_noa0000", face="a0053", head="asu_noa", x=-230, lv=2.2, id=9, sync=0},
		{"fg", ch="妃愛", size="no", mode=3, path=":fg/hiy/no/", file="hiy_noa0210", ex05="hiy_noa0010", face="a0032", head="hiy_noa", x=230, lv=2.2, id=10, sync=0},
		{"extrans", time=2000},
		{"bgm", file="bgm06"},
		{"text"},
		text = {
			vo = {
				{"vo", file="fem_hiy_10026", ch="hiy"},
			},
			ja = {
				{
					name = {"妃愛"},
					"「では、いってまいります」",
					{"rt2"},
				},
			},
		},
		linknext = "block_00001",
		line = 20,
	},
}
```
Converted
```json
{
  "ast": {
    "args": [],
    "block_00000": {
      "args": [
        {
          "args": [
            "savetitle"
          ],
          "text": "ライフタイムリスペクト"
        },
        {
          "args": [
            "bg"
          ],
          "file": "bg004a",
          "path": ":bg/",
          "sync": 0
        },
        {
          "args": [
            "fg"
          ],
          "ch": "あすみ",
          "size": "no",
          "mode": 3,
          "path": ":fg/asu/no/",
          "file": "asu_noa0200",
          "ex05": "asu_noa0000",
          "face": "a0053",
          "head": "asu_noa",
          "x": -230,
          "lv": 2.2,
          "id": 9,
          "sync": 0
        },
        {
          "args": [
            "fg"
          ],
          "ch": "妃愛",
          "size": "no",
          "mode": 3,
          "path": ":fg/hiy/no/",
          "file": "hiy_noa0210",
          "ex05": "hiy_noa0010",
          "face": "a0032",
          "head": "hiy_noa",
          "x": 230,
          "lv": 2.2,
          "id": 10,
          "sync": 0
        },
        {
          "args": [
            "extrans"
          ],
          "time": 2000
        },
        {
          "args": [
            "bgm"
          ],
          "file": "bgm06"
        },
        {
          "args": [
            "text"
          ]
        }
      ],
      "text": {
        "args": [],
        "vo": {
          "args": [
            {
              "args": [
                "vo"
              ],
              "file": "fem_hiy_10026",
              "ch": "hiy"
            }
          ]
        },
        "ja": {
          "args": [
            {
              "args": [
                "「では、いってまいります」",
                {
                  "args": [
                    "rt2"
                  ]
                }
              ],
              "name": {
                "args": [
                  "妃愛"
                ]
              }
            }
          ]
        }
      },
      "linknext": "block_00001",
      "line": 20
    }
  }
}
```
