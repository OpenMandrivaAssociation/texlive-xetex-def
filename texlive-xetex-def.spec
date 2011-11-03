# revision 16192
# category Package
# catalog-ctan /graphics/xetex/latex/xetex.def
# catalog-date 2009-11-27 22:18:13 +0100
# catalog-license lppl
# catalog-version 0.94
Name:		texlive-xetex-def
Version:	0.94
Release:	1
Summary:	Colour and graphics support for XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/xetex/latex/xetex.def
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-def.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The file xetex.def provides device-specific definitions for
colour and graphics support when running Xe(La)TeX.

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
%{_texmfdistdir}/tex/xelatex/xetex-def/xetex.def
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
