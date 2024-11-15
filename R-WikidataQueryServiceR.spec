#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-WikidataQueryServiceR
Version  : 1.0.0
Release  : 19
URL      : https://cran.r-project.org/src/contrib/WikidataQueryServiceR_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/WikidataQueryServiceR_1.0.0.tar.gz
Summary  : API Client Library for 'Wikidata Query Service'
Group    : Development/Tools
License  : MIT
Requires: R-WikipediR
Requires: R-dplyr
Requires: R-httr
Requires: R-jsonlite
Requires: R-purrr
Requires: R-ratelimitr
Requires: R-readr
Requires: R-rex
BuildRequires : R-WikipediR
BuildRequires : R-dplyr
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-purrr
BuildRequires : R-ratelimitr
BuildRequires : R-readr
BuildRequires : R-rex
BuildRequires : buildreq-R

%description
WikidataQueryServiceR
================
- [Installation](#installation)
- [Usage](#usage)
- [Example: fetching genres of a particular
movie](#example-fetching-genres-of-a-particular-movie)
- [Fetching queries from Wikidata’s examples
page](#fetching-queries-from-wikidatas-examples-page)
- [Links for learning SPARQL](#links-for-learning-sparql)
- [Additional Information](#additional-information)

%prep
%setup -q -c -n WikidataQueryServiceR
cd %{_builddir}/WikidataQueryServiceR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641148710

%install
export SOURCE_DATE_EPOCH=1641148710
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikidataQueryServiceR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikidataQueryServiceR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikidataQueryServiceR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc WikidataQueryServiceR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/WikidataQueryServiceR/DESCRIPTION
/usr/lib64/R/library/WikidataQueryServiceR/INDEX
/usr/lib64/R/library/WikidataQueryServiceR/LICENSE
/usr/lib64/R/library/WikidataQueryServiceR/Meta/Rd.rds
/usr/lib64/R/library/WikidataQueryServiceR/Meta/features.rds
/usr/lib64/R/library/WikidataQueryServiceR/Meta/hsearch.rds
/usr/lib64/R/library/WikidataQueryServiceR/Meta/links.rds
/usr/lib64/R/library/WikidataQueryServiceR/Meta/nsInfo.rds
/usr/lib64/R/library/WikidataQueryServiceR/Meta/package.rds
/usr/lib64/R/library/WikidataQueryServiceR/NAMESPACE
/usr/lib64/R/library/WikidataQueryServiceR/NEWS.md
/usr/lib64/R/library/WikidataQueryServiceR/R/WikidataQueryServiceR
/usr/lib64/R/library/WikidataQueryServiceR/R/WikidataQueryServiceR.rdb
/usr/lib64/R/library/WikidataQueryServiceR/R/WikidataQueryServiceR.rdx
/usr/lib64/R/library/WikidataQueryServiceR/help/AnIndex
/usr/lib64/R/library/WikidataQueryServiceR/help/WikidataQueryServiceR.rdb
/usr/lib64/R/library/WikidataQueryServiceR/help/WikidataQueryServiceR.rdx
/usr/lib64/R/library/WikidataQueryServiceR/help/aliases.rds
/usr/lib64/R/library/WikidataQueryServiceR/help/paths.rds
/usr/lib64/R/library/WikidataQueryServiceR/html/00Index.html
/usr/lib64/R/library/WikidataQueryServiceR/html/R.css
/usr/lib64/R/library/WikidataQueryServiceR/tests/testthat.R
/usr/lib64/R/library/WikidataQueryServiceR/tests/testthat/test-query.R
