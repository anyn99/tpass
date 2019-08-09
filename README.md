# tpass

Simple Trezor Password Manager interface for command line, inspired by pass.

Untested Beta Software! - Do not use it


## Install

Through PiP
```
pip3 install tpass
```
Manual
```
  git clone git@github:makk4/hellopass-cli.git
  python3 setup.py install --user
```
### Autocompletion
#### Bash
```
  _TPASS_COMPLETE=source tpass > tpass-complete.sh
```
and add this to your .bashrc
```
  . /path/to/tpass-complete.sh
```
#### ZSH
```
  _TPASS_COMPLETE=source_zsh tpass > tpass-complete.sh
```
and add this to your .zshrc
```
 .  ~/.oh-my-zsh/plugins/tpass-complete.sh
```
## Init
```
 tpass init
```
### Features
- Trezor Password Manager Compatible
- supports Trezor One and Trezor Model T
- cross plattform. Windows, Linux, MacOS
- Dropbox, Google Drive, Git synchronisation
- generate random Passwords and Passphrases
- use your own Wordlists of coice, default is EFF large
- list, insert, delete, edit entries
- copy passwords to clipboard or show
- export, import database in JSON, CSV
- offline usage
- do not store metadata on disk mode
### Future plans:
- Ask for password on Trezor device
- TOTP support
- Check for password leaks, online and with local DB
- Support for Ledger Nano S/X, if possible
- Staying compatible with TPM

```
Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  clip      Decrypt and copy line of entry to clipboard
  config    Configuration settings
  edit      Edit entry or tag
  exportdb  Export data base
  find      List names of passwords and tags that match names
  generate  Generate new password
  git       Call git commands on db storage
  grep      Search for pattern in decrypted entries
  importdb  Import data base
  init      Initialize new password storage
  insert    Insert entry or tag
  lock      Remove Plain Metadata file from disk
  ls        List names of passwords from tag
  rm        Remove entry or tag
  show      Decrypt and print an entry
  unlock    Unlock Storage and writes plain metadata to disk
```