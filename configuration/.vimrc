set nocompatible

filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Tagbar'
Plugin 'ctrlp.vim'
Plugin 'xml.vim'
Plugin 'html-xml-tag-matcher'
Plugin 'Markdown'
Plugin 'mattn/emmet-vim'
Plugin 'SirVer/ultisnips'
Plugin 'jameszo/vim-snippets'
Plugin 'SimpylFold'
Plugin 'w0rp/ale'
Plugin 'tomlion/vim-solidity'
Plugin 'go.vim'
Plugin 'axiaoxin/vim-json-line-format'
Plugin 'aklt/plantuml-syntax'
call vundle#end()
filetype plugin indent on

let g:ctrlp_map = '<c-a>'
let g:ctrlp_cmd = 'CtrlP'
nmap <leader>s :TagbarOpen fj<CR>
nmap <leader>f :TagbarClose<CR>
map <leader>xml :1,$!xmllint --format -<CR>
nmap yp <Plug>(ale_previous_wrap)
nmap yn <Plug>(ale_next_wrap)
nmap <Leader>y :ALEToggle<CR>
nmap <Leader>x :ALEDetail<CR>
nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR>
nmap <leader>i :call Vimporter_AutoImportSorted() <CR>
nmap <leader>e :call Vimporter_LibLookup() <CR>
nmap <leader>r :call Vimporter_SortImports() <CR>

syntax on
set nu
set encoding=utf-8
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set fileformat=unix
set wrap
set noerrorbells
set clipboard=unnamed
set foldmethod=indent
set foldlevel=9999
set smartcase

autocmd BufWritePost *.md call MdToHtml()
function! MdToHtml()
    exec "!pandoc -f markdown --metadata pagetitle=Markdown --to=html5 --highlight-style=haddock --self-contained -c $HOME/markdown-css/github.css % -o %.html"
endfunction

autocmd BufWritePost *.dot call DotToPng()
function! DotToPng()
    exec "!dot -Tpng % -o %:t.png"
endfunction
autocmd BufWritePost *.plantuml call PlantumlToPng()
function! PlantumlToPng()
    exec "!~/code/bobokit/sh/plantuml/plantuml.sh %"
endfunction

let g:ctrlp_working_path_mode = '0'

let g:vimporter_java_roots =  [
\ '/Users/James/code/docs/spring-boot-docs-1.5.8/api', 
\ '/Users/James/code/docs/spring-framework-5/javadoc-api',
\ '/Users/James/code/docs/jdk8/api']

let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-l>"
let g:UltiSnipsJumpBackwardTrgger="<c-h>"
let g:UltiSnipsListSnippets="<c-s>"

let g:ale_lint_on_enter = 0
let g:ale_sign_column_always = 0
let g:ale_set_highlights = 0
let g:ale_sign_error = '✗'
let g:ale_sign_warning = '⚡'
let g:ale_statusline_format = ['✗ %d', '⚡ %d', '✔ OK']
let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'

let g:tagbar_type_go = {
    \ 'ctagstype' : 'go',
    \ 'kinds'     : [
        \ 'p:package',
        \ 'i:imports:1',
        \ 'c:constants',
        \ 'v:variables',
        \ 't:types',
        \ 'n:interfaces',
        \ 'w:fields',
        \ 'e:embedded',
        \ 'm:methods',
        \ 'r:constructor',
        \ 'f:functions'
    \ ],
    \ 'sro' : '.',
    \ 'kind2scope' : {
        \ 't' : 'ctype',
        \ 'n' : 'ntype'
    \ },
    \ 'scope2kind' : {
        \ 'ctype' : 't',
        \ 'ntype' : 'n'
    \ },
    \ 'ctagsbin'  : 'gotags',
    \ 'ctagsargs' : '-sort -silent'
\ }

vmap y :w !pbcopy<CR><CR>
nmap p :r !pbpaste<CR><CR>
