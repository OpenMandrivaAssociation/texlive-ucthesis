# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ucthesis
# catalog-date 2009-09-27 11:52:43 +0200
# catalog-license lppl1.3
# catalog-version 3.2
Name:		texlive-ucthesis
Version:	3.2
Release:	1
Summary:	University of California thesis format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A modified version of the standard LaTeX report style that is
accepted for use with University of California PhD
dissertations and Masters theses. A sample dissertation source
and bibliography are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
