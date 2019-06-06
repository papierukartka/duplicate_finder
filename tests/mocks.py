class DataMock:
    def walk_recursively(self):
        return [
            {"../rootdir": [{"name": "poznan.txt", "size": 0}]},
            {
                "../rootdir/poznan": [
                    {"name": "test.txt", "size": 0},
                    {"name": "rot.txt", "size": 0},
                    {"name": "carrot.txt", "size": 0},
                    {"name": "poznan.txt", "size": 0},
                ]
            },
            {"../rootdir/poznan/secret": [{"name": "badtouch.jpg", "size": 0}]},
            {
                "../rootdir/wroclaw": [
                    {"name": "tomato.txt", "size": 25},
                    {"name": "pic1.txt", "size": 0},
                ]
            },
        ]
    def rm_duplicates(self):
        return [
            {"../rootdir": [{"name": "poznan.txt", "size": 0}]},
            {
                "../rootdir/poznan": [
                    {"name": "test.txt", "size": 0},
                    {"name": "rot.txt", "size": 0},
                    {"name": "carrot.txt", "size": 0},
                ]
            },
            {"../rootdir/poznan/secret": [{"name": "badtouch.jpg", "size": 0}]},
            {
                "../rootdir/wroclaw": [
                    {"name": "tomato.txt", "size": 25},
                    {"name": "pic1.txt", "size": 0},
                ]
            },
        ]