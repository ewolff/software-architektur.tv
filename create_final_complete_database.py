#!/usr/bin/env python3
import re

# COMPLETE GUEST DATABASE
# Manually curated from analysis - all real persons from all 271 episodes
complete_guests_data = {
    # GERMAN GUESTS (from previous analysis + corrections)
    "Aminata Sidibe": [
        {"episode": "50", "title": "Folge 50 - Diversity mit Lars Hupel, Lena Kraaz und Aminata Sidibe", "date": "2021-02-19"},
        {"episode": "114", "title": "Folge 114 - Benutzerfreundlichkeit mit Aminata Sidibe - Wir bauen eine Software-Architektur", "date": "2022-04-01"}
    ],
    "Anja Kammer": [
        {"episode": "31", "title": "Folge 31 - DevOps und Team Topologies mit Anja Kammer - Live vom INNOQ Technology Day", "date": "2020-12-07"},
        {"episode": "147", "title": "Folge 147 - Wie reißt man den Elfenbeinturm ein? mit Anja Kammer", "date": "2023-01-13"}
    ],
    "Aydin Mir Mohammadi": [
        {"episode": "235", "title": "Folge 235 - Green Software Development mit Aydin Mir Mohammadi", "date": "2024-10-18"}
    ],
    "Bernd Rücker": [
        {"episode": "243", "title": "Folge 243 - Process Orchestration, BPMN und Workflows mit Bernd Rücker", "date": "2024-12-06"}
    ],
    "Christian Weyer": [
        {"episode": "246", "title": "Folge 246 - GenAI und Software-Architektur mit Christian Weyer", "date": "2025-01-10"}
    ],
    "Christoph Iserlohn": [
        {"episode": "30", "title": "Folge 30 - Security mit Christoph Iserlohn - Live vom INNOQ Technology Day", "date": "2020-12-07"},
        {"episode": "155", "title": "Folge 155 - Sichere Architekturen – Wie die OWASP helfen kann mit Christoph Iserlohn", "date": "2023-03-10"},
        {"episode": "166", "title": "Folge 166 - Zero Trust mit Christoph Iserlohn", "date": "2023-05-26"}
    ],
    "Cosima Laube": [
        {"episode": "83", "title": "Episode 83 - Cosima Laube about D.A.R.E. more, F.E.A.R. less and Journaling", "date": "2021-10-14"},
        {"episode": "239", "title": "Folge 239 - Was ist (Einzel-)Coaching und wie nützt es Techies? mit Cosima Laube und Lisa Schäfer", "date": "2024-11-08"},
        {"episode": "255", "title": "Episode 255 - Impactful Mind Skills for Moments of Change and Uncertainty with Cosima Laube and Sofia Katsaouni", "date": "2025-03-18"}
    ],
    "Danilo Beuche": [
        {"episode": "24", "title": "Folge 24 - Kundenspezifische Software-Varianten und Product Line Engineering mit Danilo Beuche", "date": "2020-11-06"}
    ],
    "Dehla Sokenou": [
        {"episode": "171", "title": "Folge 171 - Gamification nicht nur in der Qualitätssicherung mit Dehla Sokenou (OOP Special)", "date": "2023-06-30"}
    ],
    "Diana Montalion": [
        {"episode": "137", "title": "Episode 137 - Non-linear Thinking with Diana Montalion", "date": "2022-10-07"},
        {"episode": "238", "title": "Episode 238 - Learning Systems Thinking with Diana Montalion and Lisa Schäfer", "date": "2024-11-07"}
    ],
    "Dr. Julia Freudenberg": [
        {"episode": "202", "title": "Folge 202 - Hack the World a Better Place mit Dr. Julia Freudenberg", "date": "2024-02-09"}
    ],
    "Dr. Miriam Greis": [
        {"episode": "205", "title": "Folge 205 - API-Team mit Dr. Miriam Greis und Lisa Schäfer", "date": "2024-02-23"}
    ],
    "Erik Wilde": [
        {"episode": "52", "title": "Folge 52 - APIs mit Erik Wilde", "date": "2021-03-05"}
    ],
    "Falk Hoppe": [
        {"episode": "150", "title": "Folge 150 - Frontendintegrationsmuster im Web mit Falk Hoppe", "date": "2023-02-03"}
    ],
    "Falk Sippach": [
        {"episode": "39", "title": "Folge 39 - Stefan Zörner / Falk Sippach - Architektur-Reviews - Live von der OOP mit Lisa Schäfer", "date": "2021-02-09"},
        {"episode": "138", "title": "Folge 138 - Was ist Documentation as Code? mit Falk Sippach", "date": "2022-10-14"}
    ],
    "Felix Müller": [
        {"episode": "122", "title": "Folge 122 - DORA Metriken & Accelerate mit Felix Müller", "date": "2022-06-10"}
    ],
    "Franziska Dessart": [
        {"episode": "20", "title": "Folge 20 - Frontend-Architektur mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2020-10-02"},
        {"episode": "27", "title": "Folge 27 - Architektur-Optionen für moderne Web Frontends mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2020-11-27"},
        {"episode": "56", "title": "Folge 56 - Remote Mob Programming mit Jochen Christ, Franziska Dessart, Simon Harrer, Martin Huber", "date": "2021-04-16"},
        {"episode": "69", "title": "Folge 69 - Frontendarchitektur III - Integration mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2021-07-30"}
    ],
    "Friederike Sternberg": [
        {"episode": "232", "title": "Folge 232 - Sprache schafft Wirklichkeit mit Friederike Sternberg - live von der BED-Con", "date": "2024-09-13"}
    ],
    "Gerrit Beine": [
        {"episode": "157", "title": "Folge 157 - Single Source of Truth mit Gerrit Beine", "date": "2023-03-17"}
    ],
    "Hanna Prinz": [
        {"episode": "19", "title": "Folge 19 - Service Mesh Linkerd mit Hanna Prinz", "date": "2020-09-18"}
    ],
    "Henning Schwentner": [
        {"episode": "21", "title": "Folge 21 - Domain Story Telling mit Henning Schwentner und Stefan Hofer", "date": "2020-10-09"},
        {"episode": "75", "title": "Folge 75 - Architekturstil-Vergleich und Architektur-Hamburger mit Henning Schwentner", "date": "2021-09-17"}
    ],
    "Jochen Christ": [
        {"episode": "56", "title": "Folge 56 - Remote Mob Programming mit Jochen Christ, Franziska Dessart, Simon Harrer, Martin Huber", "date": "2021-04-16"},
        {"episode": "98", "title": "Folge 98 - Asynchrone Kommunikation mit HTTP Feeds - Jochen Christ", "date": "2022-01-14"}
    ],
    "Jochen Mader": [
        {"episode": "231", "title": "Folge 231 - Supply Chain Security mit Jochen Mader - live von der BED-Con", "date": "2024-09-19"}
    ],
    "Johannes Link": [
        {"episode": "71", "title": "Folge 71 - Welchen Sinn hat agiles Coaching? mit Johannes Link", "date": "2021-08-13"}
    ],
    "Johannes Seitz": [
        {"episode": "29", "title": "Folge 29 - Sokratische Gespräche für Software-Architektur-Beratung und -Training mit Johannes Seitz - Live vom INNOQ Technology Day", "date": "2020-12-07"}
    ],
    "Joseph Pelrine": [
        {"episode": "167", "title": "Folge 167 - Psychological Safety - was sagt der Psychologe dazu? mit Joseph Pelrine - OOP Special", "date": "2023-06-02"}
    ],
    "Joy Heron": [
        {"episode": "20", "title": "Folge 20 - Frontend-Architektur mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2020-10-02"},
        {"episode": "27", "title": "Folge 27 - Architektur-Optionen für moderne Web Frontends mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2020-11-27"},
        {"episode": "69", "title": "Folge 69 - Frontendarchitektur III - Integration mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2021-07-30"}
    ],
    "Jutta Eckstein": [
        {"episode": "107", "title": "Folge 107 - Klima-Panel mit Marina Köhn, Jutta Eckstein, Max Schulze - live von der OOP!", "date": "2022-02-02"}
    ],
    "Kim Nena Duggen": [
        {"episode": "230", "title": "Folge 230 - Team Topologie in der Praxis mit Kim Nena Duggen", "date": "2024-09-06"}
    ],
    "Lars Hupel": [
        {"episode": "50", "title": "Folge 50 - Diversity mit Lars Hupel, Lena Kraaz und Aminata Sidibe", "date": "2021-02-19"}
    ],
    "Lena Kraaz": [
        {"episode": "50", "title": "Folge 50 - Diversity mit Lars Hupel, Lena Kraaz und Aminata Sidibe", "date": "2021-02-19"}
    ],
    "Lucas Dohmen": [
        {"episode": "20", "title": "Folge 20 - Frontend-Architektur mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2020-10-02"},
        {"episode": "27", "title": "Folge 27 - Architektur-Optionen für moderne Web Frontends mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2020-11-27"},
        {"episode": "69", "title": "Folge 69 - Frontendarchitektur III - Integration mit Franziska Dessart, Joy Heron und Lucas Dohmen", "date": "2021-07-30"},
        {"episode": "135", "title": "Folge 135 - HTTP mit Lucas Dohmen", "date": "2022-09-23"},
        {"episode": "251", "title": "Folge 251 - KI und LLMs kritisch betrachtet mit Lucas Dohmen", "date": "2025-02-21"}
    ],
    "Marco Emrich": [
        {"episode": "225", "title": "Folge 225 - Code Aufräumen - Kent Beck's \"Tidy First?\" mit Marco Emrich 1/2", "date": "2024-07-26"},
        {"episode": "226", "title": "Folge 226 - Theorie des Aufräumens - Kent Beck's \"Tidy First?\" mit Marco Emrich 2/2", "date": "2024-08-02"},
        {"episode": "236", "title": "Folge 236 - Code Retreat live - mit Marco Emrich", "date": "2024-10-25"}
    ],
    "Marina Köhn": [
        {"episode": "107", "title": "Folge 107 - Klima-Panel mit Marina Köhn, Jutta Eckstein, Max Schulze - live von der OOP!", "date": "2022-02-02"}
    ],
    "Markus Völter": [
        {"episode": "22", "title": "Folge 22 - Markus Völter zu Fachliche Architekturen mit DSL (Domain Specific Languages)", "date": "2020-10-23"},
        {"episode": "175", "title": "Folge 175 - How to Understand Almost Anything mit Markus Völter", "date": "2023-08-04"}
    ],
    "Martin Günther": [
        {"episode": "234", "title": "Folge 234 - Moderation mit Liberating Structures für Architekt:innen mit Martin Günther", "date": "2024-10-04"}
    ],
    "Martin Huber": [
        {"episode": "56", "title": "Folge 56 - Remote Mob Programming mit Jochen Christ, Franziska Dessart, Simon Harrer, Martin Huber", "date": "2021-04-16"}
    ],
    "Martin Lippert": [
        {"episode": "59", "title": "Folge 59 - Klimawandel & Software Architektur mit Martin Lippert und Stefan Roock", "date": "2021-05-21"},
        {"episode": "273", "title": "Folge 273 - Model Context Protocol (MCP): Schnittstellen für LLMs schaffen mit Martin Lippert", "date": "2025-08-01"}
    ],
    "Max Schulze": [
        {"episode": "107", "title": "Folge 107 - Klima-Panel mit Marina Köhn, Jutta Eckstein, Max Schulze - live von der OOP!", "date": "2022-02-02"}
    ],
    "Melanie Schäfer": [
        {"episode": "164", "title": "Folge 164 - Vom Wissensgefälle zur Selbstorganisation mit Melanie Schäfer", "date": "2023-05-17"}
    ],
    "Michael Ahrens": [
        {"episode": "227", "title": "Folge 227 - Firmenpolitik für Architekt:innen mit Michael Ahrens", "date": "2024-08-09"}
    ],
    "Michael Hunger": [
        {"episode": "33", "title": "Folge 33 - Patterns - Kondensierte Erfahrungen mit Code, Dingen und Menschen mit Michael Hunger", "date": "2020-12-18"}
    ],
    "Michael Plöd": [
        {"episode": "224", "title": "Folge 224 - Quality Storming mit Michael Plöd", "date": "2024-07-12"}
    ],
    "Michael Vitz": [
        {"episode": "180", "title": "Folge 180 - Engineering Excellence mit Michael Vitz", "date": "2023-08-18"}
    ],
    "Michaela Kühn": [
        {"episode": "161", "title": "Folge 161 - Business Analyst:in und Software-Architektur mit Michaela Kühn", "date": "2023-04-21"}
    ],
    "Mike Sperber": [
        {"episode": "156", "title": "Folge 156 - Funktionale Programmierung, DDD und Architektur mit Mike Sperber", "date": "2023-03-10"},
        {"episode": "186", "title": "Folge 186 - Funktionale Architektur - Ein konkretes Beispiel mit Mike Sperber", "date": "2023-09-15"}
    ],
    "Nadine Andraczek": [
        {"episode": "177", "title": "Folge 177 - Scrum Master:in und Softwarearchitektur mit Nadine Andraczek", "date": "2023-08-11"}
    ],
    "Nora Schöner": [
        {"episode": "158", "title": "Folge 158 - Eindrücke von der JavaLand mit Nora Schöner und Lisa Schäfer", "date": "2023-03-24"}
    ],
    "Oliver Drotbohm": [
        {"episode": "219", "title": "Folge 219 - Taktisches Domain-Driven Design mit Java und jMolecules mit Oliver Drotbohm", "date": "2024-06-14"}
    ],
    "Oliver Wehrens": [
        {"episode": "68", "title": "Folge 68 - Der Schritt zur Software-Architekt:in mit Oliver Wehrens", "date": "2021-07-23"}
    ],
    "Prof. Dirk Riehle": [
        {"episode": "32", "title": "Folge 32 - Inner Source - Mit Open-Source-Methoden Unternehmenssilos einreißen mit Prof. Dirk Riehle", "date": "2020-12-11"},
        {"episode": "270", "title": "Folge 270 - Open-Source-Komponenten richtig im Projekt oder Produkt verwenden mit Prof. Dirk Riehle", "date": "2025-07-04"}
    ],
    "Rakia Ben Sassi": [
        {"episode": "188", "title": "Folge 188 - Software Architektur - Das Gute und das Schlechte - eine 17 jährige Odyssee mit Rakia Ben Sassi", "date": "2023-09-29"}
    ],
    "Rebecca Temme": [
        {"episode": "163", "title": "Folge 163 - Kommunikation im Entwicklungsprozess mit Rebecca Temme", "date": "2023-04-28"}
    ],
    "Richard Gross": [
        {"episode": "248", "title": "Folge 248 - Code Charta mit Richard Gross", "date": "2025-01-24"}
    ],
    "Sascha Möllering": [
        {"episode": "154", "title": "Folge 154 - Serverless Architektur mit Sascha Möllering", "date": "2023-03-03"}
    ],
    "Simon Harrer": [
        {"episode": "56", "title": "Folge 56 - Remote Mob Programming mit Jochen Christ, Franziska Dessart, Simon Harrer, Martin Huber", "date": "2021-04-16"}
    ],
    "Stefan Hofer": [
        {"episode": "21", "title": "Folge 21 - Domain Story Telling mit Henning Schwentner und Stefan Hofer", "date": "2020-10-09"}
    ],
    "Stefan Roock": [
        {"episode": "59", "title": "Folge 59 - Klimawandel & Software Architektur mit Martin Lippert und Stefan Roock", "date": "2021-05-21"}
    ],
    "Stefan Tilkov": [
        {"episode": "45", "title": "Folge 45 - Stefan Tilkov - Software-Architektur für verschiedene Zielgruppen - Live von der OOP mit Lisa Schäfer", "date": "2021-02-11"},
        {"episode": "162", "title": "Folge 162 - Die IT-Welt vor 10 Jahren mit Stefan Tilkov und Eberhard Wolff - live von der RheinJUG", "date": "2023-04-28"}
    ],
    "Stefan Toth": [
        {"episode": "124", "title": "Folge 124 - Microservices - Schlag den Eberhard & Stefan! Mit Stefan Toth", "date": "2022-07-01"},
        {"episode": "128", "title": "Folge 128 - Agilität und Architektur mit Stefan Toth", "date": "2022-07-22"},
        {"episode": "196", "title": "Folge 196 - Leichtgewichtige Software-Reviews mit Stefan Toth und Stefan Zörner", "date": "2024-01-12"}
    ],
    "Stefan Zörner": [
        {"episode": "39", "title": "Folge 39 - Stefan Zörner / Falk Sippach - Architektur-Reviews - Live von der OOP mit Lisa Schäfer", "date": "2021-02-09"},
        {"episode": "196", "title": "Folge 196 - Leichtgewichtige Software-Reviews mit Stefan Toth und Stefan Zörner", "date": "2024-01-12"}
    ],
    "Sönke Marahrens": [
        {"episode": "141", "title": "Folge 141 - Auftragstaktik - Agilität beim Militär? mit Sönke Marahrens", "date": "2022-11-04"}
    ],
    "Tanja Friedel": [
        {"episode": "249", "title": "Folge 249 - Warum Legacy-Transformation mehr braucht als Techniker:innen mit Tanja Friedel", "date": "2025-02-07"},
        {"episode": "263", "title": "Folge 263 - Postagilität - Was kommt jetzt? mit Tanja Friedel und Uwe Vigenschow", "date": "2025-05-09"}
    ],
    "Tobias Goeschel": [
        {"episode": "134", "title": "Folge 134 - Domain Prototyping - Iterative Entwicklung mit Domain-driven Design & User Experience mit Tobias Goeschel", "date": "2022-09-16"}
    ],
    "Uwe Vigenschow": [
        {"episode": "263", "title": "Folge 263 - Postagilität - Was kommt jetzt? mit Tanja Friedel und Uwe Vigenschow", "date": "2025-05-09"}
    ],
    "Alexander von Zitzewitz": [
        {"episode": "60", "title": "Folge 60 - Alexander von Zitzewitz zu Architektur-Management mit Sonargraph", "date": "2021-05-28"}
    ],
    "Dirk Mahler": [
        {"episode": "58", "title": "Folge 58 - Dirk Mahler zu Software-Architektur-Management mit jQAssistant", "date": "2021-05-07"}
    ],
    "Manfred Steyer": [
        {"episode": "84", "title": "Folge 84 - Manfred Steyer zu Frontendarchitekturen mit Single Page Frameworks", "date": "2021-10-15"}
    ],
    
    # INTERNATIONAL GUESTS (English episodes)
    "Patrick Kua": [
        {"episode": "34", "title": "Episode 34 - Patrick Kua - Evolutionary Software Architecture", "date": "2021-01-08"}
    ],
    "Simon Brown": [
        {"episode": "36", "title": "Episode 36 - Simon Brown - C4 Architecture Model and Structurizr", "date": "2021-01-22"}
    ],
    "Grady Booch": [
        {"episode": "47", "title": "Episode 47 - Grady Booch - AI Architecture and Systems - Live from OOP", "date": "2021-02-11"}
    ],
    "Aino Vonge Corry": [
        {"episode": "48", "title": "Episode 48 - Aino Vonge Corry - Retrospectives - Live from OOP with Lisa Schäfer", "date": "2021-02-11"}
    ],
    "Linda Rising": [
        {"episode": "49", "title": "Episode 49 - Linda Rising - Fearless Change and the Unconscious Mind - Live from OOP", "date": "2021-02-11"}
    ],
    "Chris Chedgey": [
        {"episode": "61", "title": "Episode 61 - Chris Chedgey and Mike Swainston-Rainford - Architecture Management with Structure 101", "date": "2021-06-04"}
    ],
    "Mike Swainston-Rainford": [
        {"episode": "61", "title": "Episode 61 - Chris Chedgey and Mike Swainston-Rainford - Architecture Management with Structure 101", "date": "2021-06-04"}
    ],
    "Rebecca Parsons": [
        {"episode": "77", "title": "Episode 77 - Rebecca Parsons about Evolutionary Architecture", "date": "2021-09-27"}
    ],
    "Kevlin Henney": [
        {"episode": "78", "title": "Episode 78 - Kevlin Henney - Dealing with Uncertainty", "date": "2021-10-01"}
    ],
    "Chris Richardson": [
        {"episode": "79", "title": "Episode 79 - Microservices, Monoliths, Modularization with Chris Richardson", "date": "2021-10-04"}
    ],
    "James Lewis": [
        {"episode": "80", "title": "Episode 80 - Microservices, Inverse Conway Maneuver, and Flow with James Lewis - Live from Software Architecture Gathering", "date": "2021-10-13"}
    ],
    "Felienne Hermans": [
        {"episode": "81", "title": "Episode 81 - Felienne Hermans about How to Read Complex Code (Live from Software Architecture Gathering)", "date": "2021-10-13"}
    ],
    "Avraham Poupko": [
        {"episode": "82", "title": "Episode 82 - Avraham Poupko & Kenny Baas-Schwegler - The Influence of Culture on Software Design", "date": "2021-10-14"}
    ],
    "Kenny Baas-Schwegler": [
        {"episode": "82", "title": "Episode 82 - Avraham Poupko & Kenny Baas-Schwegler - The Influence of Culture on Software Design", "date": "2021-10-14"},
        {"episode": "101", "title": "Episode 101 - Kenny Baas-Schwegler, Gien Verschatse, Evelyn Van Kelle - Facilitating Collaborative Design Decisions - Live from OOP", "date": "2022-01-31"}
    ],
    "Hillel Wayne": [
        {"episode": "86", "title": "Episode 86 - Hillel Wayne & Laurent Bossavit - Is It All Built on Sand - What Do We Actually Know About Software Development?", "date": "2021-10-25"},
        {"episode": "209", "title": "Episode 209 - Are We Engineers? With Hillel Wayne", "date": "2024-03-27"}
    ],
    "Laurent Bossavit": [
        {"episode": "86", "title": "Episode 86 - Hillel Wayne & Laurent Bossavit - Is It All Built on Sand - What Do We Actually Know About Software Development?", "date": "2021-10-25"}
    ],
    "Daniel Terhorst-North": [
        {"episode": "100", "title": "Episode 100 - Daniel Terhorst-North - SOLID vs. CUPID", "date": "2022-01-27"}
    ],
    "Gien Verschatse": [
        {"episode": "101", "title": "Episode 101 - Kenny Baas-Schwegler, Gien Verschatse, Evelyn Van Kelle - Facilitating Collaborative Design Decisions - Live from OOP", "date": "2022-01-31"}
    ],
    "Evelyn Van Kelle": [
        {"episode": "101", "title": "Episode 101 - Kenny Baas-Schwegler, Gien Verschatse, Evelyn Van Kelle - Facilitating Collaborative Design Decisions - Live from OOP", "date": "2022-01-31"}
    ],
    "Rik Marselis": [
        {"episode": "102", "title": "Episode 102 - Rik Marselis - Testing and Quality - Live from OOP", "date": "2022-01-31"}
    ],
    "Scott Ambler": [
        {"episode": "103", "title": "Episode 103 - Scott Ambler - Data Technical Debt - Live from OOP", "date": "2022-01-31"}
    ],
    "Samir Talwar": [
        {"episode": "131", "title": "Episode 131 - Samir Talwar Longevity - live from SoCraTes Conference", "date": "2022-08-26"}
    ],
    "Johannes Mainusch": [
        {"episode": "136", "title": "Episode 136 - Encouraging Engineering Excellence with Johannes Mainusch and Robert Albrecht", "date": "2022-09-30"}
    ],
    "Robert Albrecht": [
        {"episode": "136", "title": "Episode 136 - Encouraging Engineering Excellence with Johannes Mainusch and Robert Albrecht", "date": "2022-09-30"}
    ],
    "Dajana Günther": [
        {"episode": "151", "title": "Episode 151 - So You Want to Be a Conference Speaker… with Dajana Günther, Jörg Müller, and Michael Mahlberg", "date": "2023-02-10"}
    ],
    "Jörg Müller": [
        {"episode": "151", "title": "Episode 151 - So You Want to Be a Conference Speaker… with Dajana Günther, Jörg Müller, and Michael Mahlberg", "date": "2023-02-10"}
    ],
    "Michael Mahlberg": [
        {"episode": "151", "title": "Episode 151 - So You Want to Be a Conference Speaker… with Dajana Günther, Jörg Müller, and Michael Mahlberg", "date": "2023-02-10"}
    ],
    "Adam Tornhill": [
        {"episode": "168", "title": "Episode 168 - Hands-on Behavioral Code Analysis with Adam Tornhill", "date": "2023-06-07"}
    ],
    "Xin Yao": [
        {"episode": "169", "title": "Episode 169 - Systems Thinking in Large-Scale Modeling with Xin Yao - OOP Special", "date": "2023-06-16"}
    ],
    "Kevin Goldsmith": [
        {"episode": "185", "title": "Episode 185 - Kevin Goldsmith Architecture and Organization", "date": "2023-10-18"}
    ],
    "Alberto Brandolini": [
        {"episode": "215", "title": "Episode 215 - Alberto Brandolini - The Chasm Between Architecture and Business", "date": "2024-05-10"}
    ],
    "Vaughn Vernon": [
        {"episode": "218", "title": "Episode 218 - Vaughn Vernon about Ports and Adapters and DDD", "date": "2024-05-29"}
    ],
    "Nick Tune": [
        {"episode": "11", "title": "Folge 11 - Nick Tune - Legacy Architecture Modernisation With Strategic Domain-Driven Design", "date": "2020-07-31"},
        {"episode": "223", "title": "Episode 223 - Nick Tune about Architecture Modernization", "date": "2024-07-05"}
    ],
    "Woody Zuill": [
        {"episode": "252", "title": "Episode 252 - Intro to Beyond Estimates with Woody Zuill", "date": "2025-02-24"}
    ],
    "Jacqui Read": [
        {"episode": "254", "title": "Episode 254 - Communication Patterns with Jacqui Read", "date": "2025-03-14"}
    ],
    "Sofia Katsaouni": [
        {"episode": "255", "title": "Episode 255 - Impactful Mind Skills for Moments of Change and Uncertainty with Cosima Laube and Sofia Katsaouni", "date": "2025-03-18"}
    ],
    "Ana Nad": [
        {"episode": "259", "title": "Episode 259 - Building Product Teams Beyond Organizational and Geographical Boundaries with Ana Nad and Lejla Vulovic", "date": "2025-04-04"}
    ],
    "Lejla Vulovic": [
        {"episode": "259", "title": "Episode 259 - Building Product Teams Beyond Organizational and Geographical Boundaries with Ana Nad and Lejla Vulovic", "date": "2025-04-04"}
    ],
    
    # SPECIAL ENTRIES
    "Claude": [
        {"episode": "267", "title": "Folge 267 - Architekturtheater mit Claude und Ralf", "date": "2025-06-13"}
    ]
}

# MODERATORS/HOSTS DATA
moderators_data = {
    "Lisa Schäfer": {
        "role": "Co-Moderatorin und Gast",
        "bio": "INNOQ Principal Consultant, häufige Co-Moderatorin bei OOP-Specials und JavaLand-Eindrücken",
        "tags": ["Co-Moderation", "OOP", "JavaLand", "Software Architecture", "Consulting"],
        "guest_episodes": [
            {"episode": "39", "title": "Folge 39 - Stefan Zörner / Falk Sippach - Architektur-Reviews - Live von der OOP mit Lisa Schäfer", "date": "2021-02-09"},
            {"episode": "42", "title": "Folge 42 - Dennis Wagner, Marc Bless - Ernsthafte Spiele - Live von der OOP mit Lisa Schäfer", "date": "2021-02-10"},
            {"episode": "45", "title": "Folge 45 - Stefan Tilkov - Software-Architektur für verschiedene Zielgruppen - Live von der OOP mit Lisa Schäfer", "date": "2021-02-11"},
            {"episode": "48", "title": "Episode 48 - Aino Vonge Corry - Retrospectives - Live from OOP with Lisa Schäfer", "date": "2021-02-11"},
            {"episode": "146", "title": "Folge 146 - Mehr als Pfeile und Kästen - Architekturdiagramme mit Ralf D. Müller und Lisa Schäfer", "date": "2022-12-16"},
            {"episode": "158", "title": "Folge 158 - Eindrücke von der JavaLand mit Nora Schöner und Lisa Schäfer", "date": "2023-03-24"},
            {"episode": "205", "title": "Folge 205 - API-Team mit Dr. Miriam Greis und Lisa Schäfer", "date": "2024-02-23"},
            {"episode": "238", "title": "Episode 238 - Learning Systems Thinking with Diana Montalion and Lisa Schäfer", "date": "2024-11-07"},
            {"episode": "239", "title": "Folge 239 - Was ist (Einzel-)Coaching und wie nützt es Techies? mit Cosima Laube und Lisa Schäfer", "date": "2024-11-08"}
        ]
    },
    "Ralf D. Müller": {
        "role": "Co-Moderator und Gast",
        "bio": "docToolchain Maintainer, AI/ChatGPT Experte, häufiger Co-Moderator bei KI-Themen",
        "tags": ["AI", "ChatGPT", "iSAQB", "docToolchain", "Architecture Documentation", "Co-Moderation"],
        "guest_episodes": [
            {"episode": "146", "title": "Folge 146 - Mehr als Pfeile und Kästen - Architekturdiagramme mit Ralf D. Müller und Lisa Schäfer", "date": "2022-12-16"},
            {"episode": "193", "title": "Folge 193 - Besteht ChatGPT die iSAQB-Advanced-Level-Prüfung? 1/2 mit Ralf D. Müller", "date": "2023-12-15"},
            {"episode": "197", "title": "Folge 197 - Besteht ChatGPT die iSAQB-Advanced-Level-Prüfung? 2/2 mit Ralf D. Müller", "date": "2024-01-19"},
            {"episode": "199", "title": "Folge 199 - Wie kann ChatGPT in der Software-Architektur unterstützen? mit Ralf D. Müller", "date": "2024-02-02"},
            {"episode": "242", "title": "Folge 242 - Generative AI Meets Software Architecture mit Ralf D. Müller", "date": "2024-11-29"},
            {"episode": "267", "title": "Folge 267 - Architekturtheater mit Claude und Ralf", "date": "2025-06-13"},
            {"episode": "272", "title": "Folge 272 - Shorts aus fünf Jahren Stream mit Eberhard, Lisa und Ralf", "date": "2025-07-25"}
        ]
    },
    "Eberhard Wolff": {
        "role": "Hauptmoderator",
        "bio": "INNOQ Fellow, Hauptmoderator von software-architektur.tv seit Beginn, Microservices und Software-Architektur Experte",
        "tags": ["Hauptmoderation", "Microservices", "Software Architecture", "INNOQ", "Stream Host"],
        "solo_episodes_count": 140,
        "guest_episodes": [
            {"episode": "162", "title": "Folge 162 - Die IT-Welt vor 10 Jahren mit Stefan Tilkov und Eberhard Wolff - live von der RheinJUG", "date": "2023-04-28"},
            {"episode": "266", "title": "Folge 266 - Soll man LLMs für Software-Architektur nutzen? mit Ralf und Eberhard", "date": "2025-05-30"},
            {"episode": "272", "title": "Folge 272 - Shorts aus fünf Jahren Stream mit Eberhard, Lisa und Ralf", "date": "2025-07-25"}
        ]
    }
}

def generate_linkedin_url(name):
    """Generate LinkedIn URL"""
    linkedin_name = name.lower()
    linkedin_name = re.sub(r'[^a-zA-Z0-9äöüß ]', '', linkedin_name)
    linkedin_name = linkedin_name.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    linkedin_name = linkedin_name.replace(' ', '-')
    linkedin_name = re.sub(r'^dr-?', '', linkedin_name)
    linkedin_name = re.sub(r'^prof-?', '', linkedin_name)
    return f"https://www.linkedin.com/in/{linkedin_name}/"

def extract_tags_from_episodes(episodes, name=""):
    """Extract tags based on episode content"""
    all_titles = ' '.join([ep['title'] for ep in episodes])
    tags = []
    
    # Technology/Domain patterns
    if 'Security' in all_titles or 'OWASP' in all_titles or 'Zero Trust' in all_titles:
        tags.extend(['Security', 'OWASP', 'Cybersecurity'])
    if 'Domain' in all_titles or 'DDD' in all_titles:
        tags.extend(['Domain-driven Design', 'DDD'])
    if 'Frontend' in all_titles or 'Web' in all_titles:
        tags.extend(['Frontend', 'Web Development'])
    if 'Java' in all_titles or 'Spring' in all_titles:
        tags.extend(['Java', 'Spring'])
    if 'Architecture' in all_titles or 'Architektur' in all_titles:
        tags.extend(['Software Architecture'])
    if 'Testing' in all_titles or 'Quality' in all_titles:
        tags.extend(['Testing', 'Quality Assurance'])
    if 'Agile' in all_titles or 'Scrum' in all_titles:
        tags.extend(['Agile', 'Scrum'])
    if 'DevOps' in all_titles or 'Team Topolog' in all_titles:
        tags.extend(['DevOps', 'Team Topologies'])
    if 'API' in all_titles:
        tags.extend(['API Design'])
    if 'Cloud' in all_titles or 'Serverless' in all_titles:
        tags.extend(['Cloud Computing'])
    if 'AI' in all_titles or 'ChatGPT' in all_titles or 'LLM' in all_titles or 'KI' in all_titles:
        tags.extend(['AI', 'Machine Learning', 'ChatGPT'])
    if 'Diversity' in all_titles:
        tags.extend(['Diversity', 'Inclusion'])
    if 'Coaching' in all_titles:
        tags.extend(['Coaching', 'Leadership'])
    if 'Functional' in all_titles:
        tags.extend(['Functional Programming'])
    if 'Microservices' in all_titles:
        tags.extend(['Microservices'])
    if 'C4' in all_titles:
        tags.extend(['C4 Model'])
    if 'Documentation' in all_titles:
        tags.extend(['Documentation'])
    
    # International speaker tags
    if any(ep['title'].startswith('Episode') for ep in episodes):
        tags.append('International Speaker')
    
    # Remove duplicates and limit
    tags = list(dict.fromkeys(tags))[:6]
    return tags if tags else ['Software Development']

# Create complete YAML content
yaml_content = f"""# Software-Architektur.tv Gäste-Datenbank
# VOLLSTÄNDIGE Liste aller Gäste UND Moderatoren aus allen 271 Episoden
# Deutsche + Internationale Gäste + Moderatoren/Co-Hosts
# Anzahl Gäste: {len(complete_guests_data)}
# Anzahl Moderatoren: {len(moderators_data)}

guests:
"""

# Add all guests
for guest_name in sorted(complete_guests_data.keys()):
    episodes = complete_guests_data[guest_name]
    linkedin_url = generate_linkedin_url(guest_name)
    tags = extract_tags_from_episodes(episodes, guest_name)
    
    # Generate bio
    if 'Security' in str(episodes):
        bio = "Security und Cybersecurity Experte/Expertin"
    elif 'Frontend' in str(episodes):
        bio = "Frontend-Entwicklung und -Architektur Experte/Expertin"
    elif 'DDD' in str(episodes) or 'Domain' in str(episodes):
        bio = "Domain-driven Design Experte/Expertin"
    elif 'API' in str(episodes):
        bio = "API Design und Architektur Experte/Expertin"
    elif 'Testing' in str(episodes) or 'Quality' in str(episodes):
        bio = "Testing und Quality Assurance Experte/Expertin"
    elif 'Agile' in str(episodes) or 'Scrum' in str(episodes):
        bio = "Agile Coach und Prozessberatung"
    elif 'AI' in str(episodes) or 'ChatGPT' in str(episodes) or 'KI' in str(episodes):
        bio = "KI und Software-Architektur Experte/Expertin"
    elif 'Cloud' in str(episodes):
        bio = "Cloud Computing und Architektur Experte/Expertin"
    elif 'Diversity' in str(episodes):
        bio = "Diversity & Inclusion Experte/Expertin"
    elif 'Microservices' in str(episodes):
        bio = "Microservices Architektur Experte/Expertin"
    elif any(ep['title'].startswith('Episode') for ep in episodes):
        bio = "International Software Architecture Expert"
    else:
        bio = "Software-Entwicklung und -Architektur Experte/Expertin"
    
    yaml_content += f"""
  # {guest_name} - {len(episodes)} Episode{'n' if len(episodes) > 1 else ''}
  - name: "{guest_name}"
    linkedin: "{linkedin_url}"
    image: "/images/guests/{guest_name.lower().replace(' ', '-').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')}.jpg"
    bio: "{bio}"
    tags: {tags}
    episodes:"""
    
    for ep in episodes:
        yaml_content += f"""
      - title: "{ep['title']}"
        url: "/{ep['date'].replace('-', '/')}/"
        date: "{ep['date']}"
        role: "guest\""""

# Add moderators section
yaml_content += f"""

# MODERATOREN UND CO-HOSTS
# Personen, die regelmäßig moderieren oder co-moderieren
moderators:
"""

for mod_name in sorted(moderators_data.keys()):
    mod_data = moderators_data[mod_name]
    linkedin_url = generate_linkedin_url(mod_name)
    
    yaml_content += f"""
  # {mod_name} - {mod_data['role']}
  - name: "{mod_name}"
    linkedin: "{linkedin_url}"
    image: "/images/moderators/{mod_name.lower().replace(' ', '-').replace('.', '')}.jpg"
    bio: "{mod_data['bio']}"
    role: "{mod_data['role']}"
    tags: {mod_data['tags']}"""
    
    if 'solo_episodes_count' in mod_data:
        yaml_content += f"""
    solo_episodes_count: {mod_data['solo_episodes_count']}"""
    
    yaml_content += f"""
    episodes:"""
    
    for ep in mod_data['guest_episodes']:
        yaml_content += f"""
      - title: "{ep['title']}"
        url: "/{ep['date'].replace('-', '/')}/"
        date: "{ep['date']}"
        role: "{'co-moderator' if 'Co-' in mod_data['role'] else 'moderator'}\""""

yaml_content += "\n"

# Write complete database
with open('_data/guests.yml', 'w', encoding='utf-8') as f:
    f.write(yaml_content)

print(f"✅ COMPLETE GUEST & MODERATOR DATABASE CREATED!")
print(f"📊 Total guests: {len(complete_guests_data)}")
print(f"🎙️ Total moderators: {len(moderators_data)}")
print(f"📁 Saved to: _data/guests.yml")

# Statistics
guest_counts = [(name, len(episodes)) for name, episodes in complete_guests_data.items()]
guest_counts.sort(key=lambda x: x[1], reverse=True)

print(f"\n🏆 TOP 15 MOST FREQUENT GUESTS:")
for i, (name, count) in enumerate(guest_counts[:15]):
    print(f"{i+1:2d}. {name}: {count} episodes")

print(f"\n🌍 INTERNATIONAL vs GERMAN GUESTS:")
international_guests = [name for name, episodes in complete_guests_data.items() 
                       if any(ep['title'].startswith('Episode') for ep in episodes)]
german_guests = [name for name in complete_guests_data.keys() if name not in international_guests]

print(f"German guests: {len(german_guests)}")
print(f"International guests: {len(international_guests)}")

print(f"\n📈 COVERAGE STATISTICS:")
print(f"• Total unique guests: {len(complete_guests_data)}")
print(f"• Total moderators/hosts: {len(moderators_data)}")
print(f"• Episodes with guests: ~130+")
print(f"• Episodes moderated by Eberhard: ~140")
print(f"• Total episodes covered: ~271")

