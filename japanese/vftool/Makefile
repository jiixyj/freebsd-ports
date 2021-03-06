# Created by: KIRIYAMA Kazuhiko <kiri@kiri.toba-cmt.ac.jp>
# $FreeBSD$

PORTNAME=	vftool
PORTVERSION=	1.2
PORTREVISION=	1
CATEGORIES=	japanese print
MASTER_SITES=	ftp://ftp.math.s.chiba-u.ac.jp/tex/ \
		${MASTER_SITE_LOCAL}
MASTER_SITE_SUBDIR=	kiri
DISTFILES=	${DISTNAME}${EXTRACT_SUFX} \
		plib13-euc.tar.gz \
		jtex-1.52.tar.gz
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Virtual font kit (n2a,a2n,a2bk,p2pn)

BUILD_DEPENDS=	${AFMDIR}/GothicBBB-Medium-H:${PORTSDIR}/japanese/japaneseAFM

ALL_TARGET=	n2a a2n a2bk p2pn
SCRIPTS_ENV=	MV=${MV} SED=${SED} AFMDIR=${AFMDIR} JFMDIR=${JFMDIR}
MAKE_ENV=	AFM=${AFMDIR} JFM=${JFMDIR}

AFMDIR=		${PREFIX}/share/fonts/afm
FONTSDIR=	${PREFIX}/share/fonts
JFMDIR=		${WRKDIR}/share/texmf/fonts/tfm/ptex
TARGETDIRS=	vf-n2a vf-a2n vf-a2bk vf-p2pn

NO_STAGE=	yes
.include <bsd.port.pre.mk>

.if ${ARCH} == "ia64"
BROKEN=		Coredump during build on ia64
.endif

post-extract:
	(cd ${WRKDIR}; \
		${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} ${DISTDIR}/plib13-euc.tar.gz \
			${EXTRACT_AFTER_ARGS} \
			share/texmf/fonts/tfm/ptex; \
		${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} ${DISTDIR}/jtex-1.52.tar.gz \
			${EXTRACT_AFTER_ARGS} \
			jtex-1.52/JTeXfonts/dnpfonts/mincho/tfm \
			jtex-1.52/JTeXfonts/dnpfonts/gothic/tfm; \
	)

do-install:
	@(cd ${FONTSDIR}; ${MKDIR} ${TARGETDIRS})
	@(cd ${WRKSRC}; \
	${INSTALL_PROGRAM} mka2bkvf mka2nvf mkn2avf mkp2nvf ${PREFIX}/bin; \
	)
.for t in ${TARGETDIRS}
	@${INSTALL_DATA} ${WRKSRC}/${t}/* ${FONTSDIR}/${t}
.endfor
	@${INSTALL_DATA} ${WRKSRC}/jfm/* ${FONTSDIR}/vf-a2bk
.if !defined(NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
	@(cd ${WRKSRC}; \
	${INSTALL_SCRIPT} MKASC2BKall MKASC2NTT MKNTT2ASC MKPTEX2PNTT ${DOCSDIR}; \
	${INSTALL_DATA} Makefile README vfdata.doc ${DOCSDIR}; \
	)
.endif

.include <bsd.port.post.mk>
