#!/bin/bash

git clone https://github.com/vim/vim.git
cd vim

git clone https://github.com/jameszo/bobokit.git
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Kashomon/vimporter.git ~/.vim/plugin/vimporter
git clone https://github.com/jameszo/snippets.git ~/.vim/snippets
git clone https://github.com/otsaloma/markdown-css.git ~/markdown-css
git clone https://github.com/jameszo/docs.git ~/code/docs


rm -f ~/.zshrc
cp ./bobokit/equip/cfg/zshrc ~/.zshrc
rm -f ~/.vimrc
cp ./bobokit/equip/cfg/vimrc ~/.vimrc

vim +PluginInstall +qall

cd ~/.vim/bundle/YouCompleteMe
./install.py --all

echo -e "y\n" > input.tmp
./install_ohmyzsh.sh < input.tmp
rm -f input.tmp
