# Created by: Alex Dupre <sysadmin@alexdupre.com>
# $FreeBSD$

PORTNAME=	nocc
PORTVERSION=	1.9.4
CATEGORIES=	mail www
MASTER_SITES=	SF/${PORTNAME}/NOCC/${PORTVERSION}

MAINTAINER=	ale@FreeBSD.org
COMMENT=	A webmail system which access POP3 and IMAP mail servers

OPTIONS_DEFINE=	DOCS

USE_PHP=	ctype iconv imap mbstring pcre session
WANT_PHP_WEB=	yes

SUB_FILES=	pkg-message
NO_BUILD=	yes

NOCCCOMP=	.htaccess favicon.ico robots.txt \
		action.php common.php contacts.php contacts_manager.php \
		delete.php down_mail.php download.php get_img.php \
		help.php index.php logout.php rss.php send.php \
		ckeditor classes config html js lang themes utils

PORTDOCS=	*

do-install:
	@${MKDIR} ${STAGEDIR}${WWWDIR}
.for i in ${NOCCCOMP}
	@cd ${WRKSRC} && ${COPYTREE_SHARE} ${i} ${STAGEDIR}${WWWDIR}
.endfor
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	@${INSTALL_DATA} ${WRKSRC}/docs/* ${STAGEDIR}${DOCSDIR}
	@${ECHO_CMD} "@owner ${WWWOWN}" >> ${TMPPLIST}
	@${ECHO_CMD} "@group ${WWWGRP}" >> ${TMPPLIST}
	@(cd ${WRKSRC}; ${FIND} ${NOCCCOMP} -not -type d) | ${SORT} | \
		${SED} -ne 's,^,${WWWDIR_REL}/,p' >> ${TMPPLIST}
	@(cd ${WRKSRC}; ${FIND} ${NOCCCOMP} -type d) | ${SORT} -r | \
		${SED} -ne 's,^,@dirrm ${WWWDIR_REL}/,p' >> ${TMPPLIST}
	@${ECHO_CMD} '@dirrm ${WWWDIR_REL}' >> ${TMPPLIST}
	@${ECHO_CMD} "@owner" >> ${TMPPLIST}
	@${ECHO_CMD} "@group" >> ${TMPPLIST}

.include <bsd.port.mk>
