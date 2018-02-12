"=============Colors============= 
colorscheme default		" colorscheme if you so wish
syntax enable			" enable Syntax processing


"=============Space and Tabs============= 
set tabstop=4			" number of visual spaces per TAB
set softtabstop=4		" number of spaces in tab when editing
set shiftwidth=4		" number of spaces for autoindent
set expandtab			" convert tabs into spaces
set autoindent          " automatically indent a line like the one before
filetype indent on		" load filetype-specific indent files
"set smartindent         " nicer and smarter indentation
                        " does not work with filetype indent
set backspace=indent,eol,start      " Chance backspace to the usual (non-vim) behaviour

"=============UI Config============= 
set number				" show line numbers
set showcmd				" show command in bottom bar
"set ruler               " enable a ruler, displaying line and column number
                        " unnecessary since showcmd is enabled
set cursorline			" highlight current line
set showbreak=+++       " marking wrapped lines with +++
set linebreak           " nicer line breaking/wrapping
set wildmenu			" visual autocomplete for command menu
set lazyredraw			" redraw only when necessary
set showmatch			" highlight matching bracket [{}]

"=============Searching============= 
set incsearch			" search as characters are entered
set hlsearch			" highlight matches

"=============Various===============
" switches relative to absolute line numbers when splitting vim
if has('autocmd')
augroup vimrc_linenumbering
	autocmd!
	autocmd WinLeave *
		\ if &number |
		\   set norelativenumber |
		\ endif
	autocmd BufWinEnter *
		\ if &number |
		\   set relativenumber |
		\ endif
	autocmd VimEnter *
		\ if &number |
		\   set relativenumber |
		\ endif
augroup END
endif
