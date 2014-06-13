# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ucthesis
# catalog-date 2009-09-27 11:52:43 +0200
# catalog-license lppl1.3
# catalog-version 3.2
Name:		texlive-ucthesis
Version:	3.2
Release:	7
Summary:	University of California thesis format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucthesis.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.2-2
+ Revision: 757227
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.2-1
+ Revision: 719832
- texlive-ucthesis
- texlive-ucthesis
- texlive-ucthesis

