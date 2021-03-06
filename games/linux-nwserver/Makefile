# Created by: Igor Pokrovsky <tiamat@comset.net>
# $FreeBSD$

PORTNAME=	nwserver
PORTVERSION=	1.32
PORTREVISION=	2
CATEGORIES=	games linux
MASTER_SITES=	http://nwdownloads.bioware.com/neverwinternights/linux/${PORTVERSION:S/.//}/
PKGNAMEPREFIX=	linux-
DISTNAME=	linuxserver${PORTVERSION:S/.//}

MAINTAINER=	apeiron@coitusmentis.info
COMMENT=	Neverwinter Nights Linux (x86) Dedicated Server

USE_LINUX=	yes
ONLY_FOR_ARCHS=	i386
WRKSRC=		${WRKDIR}

NO_STAGE=	yes
do-build:
	${BRANDELF} -t Linux ${WRKDIR}/nwserver

do-install:
	${INSTALL_PROGRAM} ${WRKDIR}/fixinstall ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKDIR}/nwserver ${PREFIX}/bin

.ifndef (NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
	${INSTALL_DATA} ${WRKDIR}/readme.linuxserver.txt ${DOCSDIR}
.endif

post-install:
	@${ECHO_MSG} "*******************************************************************************"
	@${ECHO_MSG} "Neverwinter Nights Dedicated Server requires original game data to run."
	@${ECHO_MSG} "Consult ${DOCSDIR}/readme.linuxserver.txt"
	@${ECHO_MSG} "for more information about required data directories."
	@${ECHO_MSG} "From directory, where you will have installed game data you can run:"
	@${ECHO_MSG} "${PREFIX}/bin/fixinstall - to check installation"
	@${ECHO_MSG} "and ${PREFIX}/bin/nwserver - to start server"
	@${ECHO_MSG} "*******************************************************************************"

.include <bsd.port.mk>
