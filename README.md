A NOTE ON DEPENDENCIES: This currently requires the [Japanese Support addon](https://ankiweb.net/shared/info/3918629684) and the [the developer version of the NHK accent addon](https://github.com/weirdalsuperfan/nhk-pronunciation/tree/patch-1).

After installing those, to install this addon, simply copy the two files in the Sanseido-Definitions folder into your Anki addons folder. Copy the two files, not the folder, i.e. place the files at the top level of the addons folder - but if you already have a bs4 folder in your addons folder, do not overwrite it; just leave it as is.

# Sanseido Definitions Plugin for Anki

This is a plugin for [Anki](http://ankisrs.net/), an open source flashcard system. It pulls simplified J-J definitions from [sanseido.net](http://www.sanseido.net)'s デイリーコンサイス国語辞典 (Daily Concise Kokugo Jiten). This is a fork from the original, the AnkiWeb page of which can be found [here](https://ankiweb.net/shared/info/1967553085).

## Usage

The plugin relies on having 2 fields,
  * Expression - The Japanese word/words/sentence to look up on sanseido
  * Sanseido - The field to insert the definition (annotated with 振り仮名) into

If you'd like to change the names of these fields, edit lines 25-26 in sanseidoDefsForAnki.py

To add definitions, find/highlight the card (or cards - works in bulk) in the Anki browser window, and click Edit > Regenerate Sanseido definitions

## Help on reading the definitions

Sanseido has some nice [辞書凡例](http://www.sanseido.biz/main/Dictionary/Hanrei/dailyJJ.aspx) (Dictionary explanatory notes) for デイリーコンサイス国語辞典. Explanation on the symbols and abbreviations used can be found in section 9, 記号・略語一覧.

## Bugs?
If the bs4 folder included here does not work for you, report it on here and I will upload the version I personally use (this is a fork, but the original only used a partial bs4 so that's what I left on GitHub even though it's different from my local copy).

Also report any bugs related to parsing multiple words on this page.

Report other bugs and issues to the original GitHub page of the addon [here](https://github.com/kqueryful/Sanseido-Definitions).

