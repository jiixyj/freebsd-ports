# $FreeBSD$

PORTNAME=	gdt
PORTVERSION=	4.0
CATEGORIES=	cad
MASTER_SITES=	SF/gds2/gds2/
DISTNAME=	${PORTNAME:U}-${PORTVERSION}

MAINTAINER=	hrs@FreeBSD.org
COMMENT=	GDS2/GDT format translator

LICENSE=	GPLv2

USES=	shebangfix perl5
USE_PERL5=	run
SHEBANG_FILES=	Examples/gdsinfo Examples/scalegds
WRKSRC=		${WRKDIR}/${PORTNAME:U}-${PORTVERSION}
PLIST_FILES=	bin/gdsinfo bin/gds2gdt bin/gdt2gds bin/scalegds

NO_STAGE=	yes
post-patch:
	${REINPLACE_CMD} -e 's,%%PREFIX%%,${PREFIX},' \
		${WRKSRC}/Examples/gdsinfo ${WRKSRC}/Examples/scalegds

pre-build:
	${INSTALL_DATA} ${FILESDIR}/Makefile ${WRKSRC}

post-install:
	${INSTALL_SCRIPT} \
		${WRKSRC}/Examples/gdsinfo \
		${WRKSRC}/Examples/scalegds \
		${PREFIX}/bin

.include <bsd.port.mk>
