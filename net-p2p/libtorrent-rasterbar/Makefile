# Created by: Doug Barton <dougb@FreeBSD.org>
# $FreeBSD$

PORTNAME=	libtorrent-rasterbar
PORTVERSION=	0.16.13
PORTREVISION=	2
CATEGORIES?=	net-p2p ipv6
MASTER_SITES=	SF/${PORTNAME:S/-rasterbar//}/${PORTNAME:S/-rasterbar//}/

MAINTAINER=	nemysis@FreeBSD.org
COMMENT?=	C++ library implementing a BitTorrent client

LICENSE=	BSD3CLAUSE

LIB_DEPENDS?=	libboost_date_time.so:${PORTSDIR}/devel/boost-libs \
		libGeoIP.so:${PORTSDIR}/net/GeoIP

USES=		compiler:c++11-lang pathfix pkgconfig iconv
USE_OPENSSL=	yes
GNU_CONFIGURE=	yes
CFLAGS+=	-w
USE_LDCONFIG=	yes

# Wrong versioning upstream
PORTSCOUT=	skipv:0.16.14

CONFIGURE_ARGS=	--disable-debug \
		--disable-static \
		--enable-dht \
		--enable-encryption \
		--enable-pool-allocators \
		--enable-deprecated-functions \
		--with-boost=${LOCALBASE} \
		--with-boost-system=boost_system \
		--enable-geoip \
		--with-libgeoip \
		--with-libiconv \
		--with-openssl=${OPENSSLBASE}

SHLIB_VER=	7
PLIST_SUB+=	SHLIB_VER="${SHLIB_VER}"

SUB_FILES=	pkg-message

PORTDOCS=	*

DOCSRCDIR1=	${WRKSRC}
DOC_FILES1=	AUTHORS README

DOCSRCDIR2=	${WRKSRC}/docs
DOCSDIR2=	${DOCSDIR}/docs
DOC_FILES2=	*.png *.jpg *.gif *.html *.rst *.css

PORTEXAMPLES=	*.cpp

OPTIONS_DEFINE=	DOCS EXAMPLES STRIP
OPTIONS_DEFAULT=	STRIP

.include <bsd.port.options.mk>

.if defined(SLAVE_PORT) && ${SLAVE_PORT:L} == "yes" && defined(USE_PYTHON)
CONFIGURE_ARGS+=	--enable-python-binding \
			--with-boost-python=boost_python
.else
CONFIGURE_ARGS+=	--disable-python-binding
.endif

post-patch:
	@${REINPLACE_CMD} -e 's|/usr/local/include|${PREFIX}/include|' \
		${WRKSRC}/Jamfile

post-install:
.if ${PORT_OPTIONS:MSTRIP}
	${STRIP_CMD} \
	${STAGEDIR}${PREFIX}/lib/libtorrent-rasterbar.so.${SHLIB_VER}
.else
	${STRIP_CMD} \
	${STAGEDIR}${PREFIX}/lib/${PYTHON_VERSION}/site-packages/libtorrent.so
.endif

	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${DOC_FILES1:S|^|${DOCSRCDIR1}/|} ${STAGEDIR}${DOCSDIR}
	@${MKDIR} ${STAGEDIR}${DOCSDIR2}
	${INSTALL_DATA} ${DOC_FILES2:S|^|${DOCSRCDIR2}/|} ${STAGEDIR}${DOCSDIR2}

	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	${INSTALL_DATA} ${PORTEXAMPLES:S|^|${WRKSRC}/examples/|} \
		${STAGEDIR}${EXAMPLESDIR}

.include <bsd.port.mk>
