Name:		texlive-ucthesis
Version:	15878
Release:	2
Summary:	University of California thesis format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A modified version of the standard LaTeX report style that is
accepted for use with University of California PhD
dissertations and Masters theses. A sample dissertation source
and bibliography are provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ucthesis/uct10.clo
%{_texmfdistdir}/tex/latex/ucthesis/uct11.clo
%{_texmfdistdir}/tex/latex/ucthesis/uct12.clo
%{_texmfdistdir}/tex/latex/ucthesis/ucthesis.cls
%doc %{_texmfdistdir}/doc/latex/ucthesis/README
%doc %{_texmfdistdir}/doc/latex/ucthesis/uctest.bib
%doc %{_texmfdistdir}/doc/latex/ucthesis/uctest.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
