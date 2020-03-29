#!/bin/sh

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Kashomon/vimporter.git ~/.vim/plugin/vimporter
git clone git@github.com:jameszo/markdown-css.git ~/markdown-css
git clone git@github.com:jameszo/docs.git ~/code/docs

#/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


brew cask install osxfuse
brew install sshfs

brew install docker
brew install docker-machine
brew install docker-swarm
brew install docker-machine-driver-xhyve
sudo chown root:wheel $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve

brew install autojump
brew cask install dash
brew cask install iterm2

brew install openjdk
sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

brew install plantuml
brew install pandoc
brew install nmap
brew install ctags-exuberant

brew install mysql-connector-c++

brew install vim
brew install cmake
brew install golang
brew install npm
brew install wget

#sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
