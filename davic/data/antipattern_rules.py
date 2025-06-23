ANTIPATTERN_RULES = {
    "Swiss Army Knife": {
        "versiones": [
            {
                "lenguajes": ["python", "java"],
                "reglas": {
                    "core": ["Multiple Interface"],
                    "reforzador": ["Swiss Army Knife Definition"]
                },
                "umbral": 1
            }
        ]
    },

    "Functional Decomposition": {
        "versiones": [
            {
                "lenguajes": ["python"],
                "reglas": {
                    "core": ["Field Private", "Procedural names"],
                    "reforzador": ["Functional Decomposition Definition"]
                },
                "umbral": 2
            },
            {
                "lenguajes": ["java"],
                "reglas": {
                    "core": ["Field Private", "Class One Method", "Procedural names"],
                    "reforzador": ["Functional Decomposition Definition"]
                },
                "umbral": 3
            }
        ]
    },

    "Spaghetti Code": {
        "versiones": [
            {
                "lenguajes": ["python"],
                "reglas": {
                    "core": [
                        "Long Method",
                        "Method No Parameter",
                        "ClassGlobalVariable",
                        "No Polymorphism"
                    ],
                    "reforzador": ["Spaghetti Code Definition"]
                },
                "umbral": 4
            },
            {
                "lenguajes": ["java"],
                "reglas": {
                    "core": [
                        "Long Method",
                        "Method No Parameter",
                        "ClassGlobalVariable",
                        "No Inheritance",
                        "No Polymorphism"
                    ],
                    "reforzador": ["Spaghetti Code Definition"]
                },
                "umbral": 5
            }
        ]
    }
}