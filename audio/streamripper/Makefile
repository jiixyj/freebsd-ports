# Created by: trevor
# $FreeBSD$

PORTNAME=	streamripper
PORTVERSION=	1.64.6
PORTREVISION=	3
CATEGORIES=	audio
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}%20%28current%29/${PORTVERSION} \
		http://gd.tuwien.ac.at/hci/cdk/:cdk
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}:DEFAULT \
		cdk-${CDK_VERSION}.tgz:cdk
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX}

MAINTAINER=	sylvio@FreeBSD.org
COMMENT=	Splits SHOUTcast stream into tracks

LIB_DEPENDS=	libmad.so:${PORTSDIR}/audio/libmad \
		libtre.so:${PORTSDIR}/textproc/libtre

OPTIONS_DEFINE=	FAAD VORBIS
OPTIONS_DEFAULT=	FAAD VORBIS

LICENSE=	GPLv2

USES=		iconv pkgconfig
NO_STAGE=	yes
USE_GNOME=	glib20
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--without-included-libmad \
		--without-included-tre \
		--with-included-argv \
		--with-included-cdk

MAN1=		streamripper.1
PLIST_FILES=	bin/streamripper

CFLAGS+=	-DANSI_PROTOTYPES
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-Lcdk-${CDK_VERSION} -L${LOCALBASE}/lib

CDK_VERSION=	5.0-20060507

.include <bsd.port.options.mk>

.if ! ${PORT_OPTIONS:MFAAD}
CONFIGURE_ARGS+=	ac_cv_lib_faad_NeAACDecDecode2=no
.else
LIB_DEPENDS+=	libfaad.so:${PORTSDIR}/audio/faad
.endif

.if ! ${PORT_OPTIONS:MVORBIS}
CONFIGURE_ARGS+=	--without-ogg
.else
LIB_DEPENDS+=	libvorbis.so:${PORTSDIR}/audio/libvorbis
.endif

post-extract:
	@cd ${WRKSRC} && ${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} \
		${DISTDIR}/cdk-${CDK_VERSION}.tgz ${EXTRACT_AFTER_ARGS}

post-patch:
	@${REINPLACE_CMD} -e '/if test/s|==|=|g ; \
		 s|-lpthread|${PTHREAD_LIBS}|g' ${WRKSRC}/configure

pre-configure:
	@cd ${WRKSRC}/cdk-${CDK_VERSION} && ${SETENV} CC="${CC}" \
		CFLAGS="${CFLAGS}" ${SH} ./configure

pre-build:
	@cd ${WRKSRC}/cdk-${CDK_VERSION} && ${SETENV} ${MAKE_ENV} \
		${MAKE} ${MAKE_FLAGS} ${MAKEFILE} ${ALL_TARGET}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/streamripper ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/streamripper.1 ${MANPREFIX}/man/man1

.include <bsd.port.mk>
