# Created by: Thomas Gellekum <tg@FreeBSD.org>
# $FreeBSD$

PORTNAME=	guile
PORTVERSION=	1.1.4
PORTREVISION=	7
CATEGORIES=	lang gnustep
MASTER_SITES=	${MASTER_SITE_GNUSTEP}
MASTER_SITE_SUBDIR=	libs
PKGNAMEPREFIX=	gnustep-
PKGNAMESUFFIX?=	${NOX11_SUFFIX}${PKGNAMESUFFIX2}
DISTNAME=	${PKGNAMEPREFIX}${PORTNAME}-${PORTVERSION}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	GNUstep interface to the GUILE scheme interpreter

LIB_DEPENDS+=	guile.21:${PORTSDIR}/lang/guile

LICENSE=	GPLv2

USE_GNUSTEP=	yes
USE_GNUSTEP_CONFIGURE=	yes
USE_GNUSTEP_BUILD=	yes
USE_GNUSTEP_INSTALL=	yes
USE_GNUSTEP_LDCONFIG=	${GNUSTEP_SYSTEM_LIBRARIES}

GNU_CONFIGURE=	yes
MAKE_FLAGS=	OPTFLAG="${CFLAGS}"
PLIST_SUB+=	GUILE_VER="${GUILE_VER}"

MAN1=	greg.1
INFO=	greg

FIXME=		Library/gg_class.m ScriptKit/Library/GuileInterpreter.m

.if defined(WITHOUT_X11)
NOX11_SUFFIX?=	-nox11
USE_GNUSTEP_BASE=	yes
PLIST_SUB+=		USEX11="@comment "
CONFLICTS?=		gnustep-guile-1.*
.else
USE_GNUSTEP_BACK=	yes
PLIST_SUB+=		USEX11=""
CONFLICTS?=		gnustep-guile-nox11-1.*
.endif

NO_STAGE=	yes
.include <bsd.port.pre.mk>

GUILE_VER!=	${MAKE} -C ${PORTSDIR}/lang/guile -V GUILE_VER

post-patch:
	${REINPLACE_CMD} -e 's|echo aout|echo elf|' \
		${WRKSRC}/Greg/configure
.for i in ${FIXME}
	${REINPLACE_CMD} -e 's|scm_catch_body_t|scm_t_catch_body|' \
		-e 's|scm_catch_handler_t|scm_t_catch_handler|' \
		-e 's|scm_intern|scm_c_define|' \
		${WRKSRC}/${i}
.endfor

pre-configure:
	${TOUCH} ${WRKSRC}/Greg/ac_nonexistent.h

post-configure:
	${MV} ${WRKSRC}/Greg/Makefile ${WRKSRC}/Greg/GNUmakefile

.include <bsd.port.post.mk>
