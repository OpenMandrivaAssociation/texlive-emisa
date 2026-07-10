%global tl_name emisa
%global tl_revision 71883

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3.0
Release:	%{tl_revision}.1
Summary:	A LaTeX package for preparing manuscripts for the journal EMISA
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/emisa
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emisa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emisa.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emisa.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The EMISA LaTeX package is provided for preparing manuscripts for
submission to EMISA (Enterprise Modelling and Information Systems
Architectures), and for preparing accepted submissions for publication
as well as for typesetting the final document by the editorial office.
Articles in EMISA are published online at EMISA in the Portable Document
Format (PDF).

