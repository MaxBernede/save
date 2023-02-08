# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kyuuh <kyuuh@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/07 10:45:43 by mbernede          #+#    #+#              #
#    Updated: 2022/12/19 11:36:41 by kyuuh            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SRCS 	:= 		main.c

RM 		:= 		rm -f

NAME	:=		test

CFLAGS	:=		-Wall -Werror -Wextra

CC		:= 		cc

OBJ_DIR	:=		./objs/

SRC_DIR	:=		./srcs/

LIBA	:=	libft/libft.a
LIBH	:=	libft/libft.h

OBJ 	:= 		$(addprefix ${OBJ_DIR},${SRCS:.c=.o})

${NAME}:	${OBJ}
	@make -C libft
	@$(CC) -o $@ $^ $(LIBA)
	@echo "SUCCESS"

all : ${NAME}

${OBJ_DIR}%.o:	${SRC_DIR}%.c $(LIBH)
	@${CC} ${CFLAGS} -o $@ -c $<

clean: 
	@make -C libft clean
	@${RM} ${OBJ}
	@echo "test cleaned"

fclean: 	clean
	@make -C libft fclean
	@${RM} ${NAME}
	@echo "full clean done"

re: 	fclean all

.PHONY:		all clean fclean re
