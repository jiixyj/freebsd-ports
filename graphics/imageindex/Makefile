# Created by: John Reynolds <johnjen@reynoldsnet.org>
# $FreeBSD$

PORTNAME=	imageindex
PORTVERSION=	1.1
PORTREVISION=	5
CATEGORIES=	graphics
MASTER_SITES=	http://www.edwinh.org/imageindex/release/ \
		http://www.reynoldsnet.org/imageindex/release/

MAINTAINER=	johnjen@reynoldsnet.org
COMMENT=	A digital photo gallery tool

RUN_DEPENDS=	\
	${LOCALBASE}/bin/Magick-config:${PORTSDIR}/graphics/ImageMagick \
	${LOCALBASE}/bin/wrjpgcom:${PORTSDIR}/graphics/jpeg \
	${LOCALBASE}/bin/mplayer:${PORTSDIR}/multimedia/mplayer \
	p5-Image-Info>=0:${PORTSDIR}/graphics/p5-Image-Info

USES=		perl5
USE_PERL5=	run
MAKE_ARGS+=	PERLPATH=${PERL}

PLIST_FILES=	bin/imageindex bin/autocaption
PORTDOCS=	README

MAN1=	imageindex.1

NO_STAGE=	yes
post-patch:
	${REINPLACE_CMD} -e 's|share/man|man| ;' ${WRKSRC}/Makefile

post-install:
.if !defined(NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README ${DOCSDIR}
.endif

.include <bsd.port.mk>
