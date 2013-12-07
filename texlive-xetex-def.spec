# revision 30729
# category Package
# catalog-ctan /graphics/xetex/latex/xetex.def
# catalog-date 2013-02-20 11:06:23 +0100
# catalog-license lppl
# catalog-version 0.95
Name:		texlive-xetex-def
Version:	0.95
Release:	3
Summary:	Colour and graphics support for XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/xetex/latex/xetex.def
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-def.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file xetex.def provides device-specific definitions for
colour and graphics support when running Xe(La)TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xetex-def/xetex.def

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
