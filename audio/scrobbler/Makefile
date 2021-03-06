# Created by: arved
# $FreeBSD$

PORTNAME?=	scrobbler
PORTVERSION=	0.3.8.1
PORTREVISION=	15
CATEGORIES=	audio
MASTER_SITES=	http://static.audioscrobbler.com/plugins/ \
		http://www.pipian.com/stuffforchat/
DISTNAME=	xmms-scrobbler-${PORTVERSION}

MAINTAINER?=	novel@FreeBSD.org
COMMENT?=	XMMS/BMP plugin for Audioscrobbler.com

LIB_DEPENDS=	libcurl.so:${PORTSDIR}/ftp/curl

CONFLICTS=	bmp-scrobbler-[0-9]* \
		xmms-scrobbler-[0-9]*

USES=		gmake pkgconfig
USE_CSTD=	gnu89
NO_STAGE=	yes
USE_BZIP2=	yes
GNU_CONFIGURE=	yes
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

SLAVEDIRS=	audio/xmms-scrobbler audio/bmp-scrobbler

.if !defined(WITH_XMMS) && !defined(WITH_BMP)
WITH_XMMS=	yes
WITH_BMP=	yes
.endif

.if defined(WITH_XMMS)
LIB_DEPENDS+=	libxmms.so:${PORTSDIR}/multimedia/xmms
PLIST_FILES+=	lib/xmms/General/libxmms_scrobbler.la \
		lib/xmms/General/libxmms_scrobbler.so
.else
CONFIGURE_ARGS+=	--disable-xmms-plugin
.endif

.if defined(WITH_BMP)
LIB_DEPENDS+=	libbeep.so:${PORTSDIR}/multimedia/beep-media-player
PLIST_FILES+=	lib/bmp/General/libbmp_scrobbler.la \
		lib/bmp/General/libbmp_scrobbler.so
.else
CONFIGURE_ARGS+=	--disable-bmp-plugin
.endif

.if defined(WITH_DEBUG)
CONFIGURE_ARGS+=	--enable-debug
.endif

.if defined(WITH_APE)
CONFIGURE_ARGS+=	--enable-prefer-ape
.endif

.if defined(WITH_ENCODINGS_PATCH)
USES+=	iconv
.endif

post-patch::
	@${REINPLACE_CMD} -e 's|echo aout|echo elf|' ${WRKSRC}/configure
.if defined(WITH_ENCODINGS_PATCH)
	@${PATCH} ${PATCH_ARGS} -p1 < ${FILESDIR}/extra-encodings-patch
.endif

pre-everything::
	@${ECHO_MSG} "You may specify the following on the command line:"
	@${ECHO_MSG} " "
	@${ECHO_MSG} "WITH_XMMS=yes to enable xmms support"
	@${ECHO_MSG} "WITH_BMP=yes to enable beep-media-player support"
	@${ECHO_MSG} "WITH_DEBUG=yes to turn on debug mode"
	@${ECHO_MSG} "WITH_APE=yes to enable ape"
	@${ECHO_MSG} "WITH_ENCODINGS_PATCH=yes to enable ID3 tags recoding support"
	@${ECHO_MSG} " "

.include <bsd.port.mk>
