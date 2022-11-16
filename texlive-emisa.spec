Name:		texlive-emisa
Version:	60068
Release:	1
Summary:	A LaTeX package for preparing manuscripts for the journal EMISA
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emisa
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emisa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emisa.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emisa.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The EMISA LaTeX package is provided for preparing manuscripts
for submission to EMISA (Enterprise Modelling and Information
Systems Architectures), and for preparing accepted submissions
for publication as well as for typesetting the final document
by the editorial office. Articles in EMISA are published online
at EMISA in the Portable Document Format (PDF).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/emisa
%{_texmfdistdir}/tex/latex/emisa
%doc %{_texmfdistdir}/doc/latex/emisa

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
