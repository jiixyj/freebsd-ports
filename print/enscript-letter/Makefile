# Created by: kline
# $FreeBSD$

PORTNAME=	enscript
PORTVERSION=	1.6.4
PORTREVISION=	5
CATEGORIES+=	print
MASTER_SITES=	http://www.codento.com/people/mtr/genscript/
PKGNAMESUFFIX=	-${PAPERSIZE}
DISTNAME=	enscript-${PORTVERSION}

MAINTAINER?=	rafan@FreeBSD.org
COMMENT=	ASCII to PostScript filter

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--disable-nls --with-media=${PS}
NO_STAGE=	yes

CONFLICTS?=	enscript-a4-* enscript-letterdj-*

INFO=		enscript
MAN1=		diffpp.1 enscript.1 sliceprint.1 states.1

PAPERSIZE?=	letter
PS?=		Letter

.if (${PAPERSIZE} != a4 && ${PAPERSIZE} != letter && ${PAPERSIZE} != letterdj)
.BEGIN:
	@${ECHO} "Error: invalid value for PAPERSIZE: \"${PAPERSIZE}\""
	@${ECHO} "Possible values are:  a4, letter, or letterdj"
	@${FALSE}
.endif

.include <bsd.port.mk>
