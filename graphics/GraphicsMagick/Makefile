# Created by: Ron van Daal
# $FreeBSD$

PORTNAME=	GraphicsMagick
PORTVERSION=	1.1.15
PORTREVISION=	5
PORTEPOCH=	1
CATEGORIES=	graphics
MASTER_SITES=	SF \
		ftp://ftp.graphicsmagick.org/pub/GraphicsMagick/1.1/
PORTSCOUT=	limit:^1\.1\.

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Fast image processing tools based on ImageMagick

CONFLICTS=	GraphicsMagick-1.[23].* GraphicsMagick1[23]-*

LIB_DEPENDS=	libfreetype.so:${PORTSDIR}/print/freetype2 \
		libfpx.so:${PORTSDIR}/graphics/libfpx \
		libjbig.so:${PORTSDIR}/graphics/jbigkit \
		libpng15.so:${PORTSDIR}/graphics/png \
		libxml2.so:${PORTSDIR}/textproc/libxml2 \
		libjasper.so:${PORTSDIR}/graphics/jasper \
		libjpeg.so:${PORTSDIR}/graphics/jpeg \
		liblcms.so:${PORTSDIR}/graphics/lcms \
		libtiff.so:${PORTSDIR}/graphics/tiff

OPTIONS_DEFINE=	Q8BIT TESTS X11 DOCS

Q8BIT_DESC=	Use 8-bit pixels (speed) instead of 16 (quality)
TESTS_DESC=	Run bundled self-tests after build

OPTIONS_DEFAULT=X11 TESTS DOCS

USES=		iconv
USE_AUTOTOOLS=	libtool
USE_BZIP2=	yes
USE_GHOSTSCRIPT=yes
GNU_CONFIGURE=	yes

.ifndef WINDOWS_FONT_DIR
# Use fonts installed by x11-fonts/webfonts by default
WINDOWS_FONT_DIR=${LOCALBASE}/lib/X11/fonts/webfonts
.endif

CONFIGURE_ARGS=	--without-perl --enable-shared --enable-static \
		--without-threads
USE_LDCONFIG=	yes

ALL_TARGET=	-j`${SYSCTL} -n hw.ncpu`

CFLAGS+=	-DPNG_DEPSTRUCT=
CPPFLAGS+=	-I${LOCALBASE}/include -I${LOCALBASE}/include/libpng15
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

test check:
	cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} ${MAKE} check

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MDOCS} == ""
# Get rid of the Makefile targets that install the documentation
# and HTML files into DOCSDIR
EXTRA_PATCHES+=	${FILESDIR}/extra-patch-Makefile.in
.endif

.if defined(WITH_WINDOWS_FONT_DIR)
CONFIGURE_ARGS+=	--with-windows-font-dir="${WINDOWS_FONT_DIR}"
.endif

.if ${PORT_OPTIONS:MX11} == ""
CONFIGURE_ARGS+=--without-x
LIB_DEPENDS+=	libwmflite.so:${PORTSDIR}/graphics/libwmf-nox11
.else
LIB_DEPENDS+=	libwmflite.so:${PORTSDIR}/graphics/libwmf
.endif

.if ${PORT_OPTIONS:MQ8BIT}
CONFIGURE_ARGS+=	--with-quantum-depth=8
PLIST_SUB+=		Q=8
.else
CONFIGURE_ARGS+=	--with-quantum-depth=16
PLIST_SUB+=		Q=16
.endif

.if ${PORT_OPTIONS:MTESTS}
post-build::	test
.else
post-build::
	#
	# You are strongly advised to run ``make test'' now
	# and report any failures to ${MAINTAINER}.
	#
.endif

.include <bsd.port.mk>
