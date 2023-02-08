SRCS 	:= 		main.c

SRC_DIR :=		./srcs/

OBJ_DIR :=		./objs/

OBJ 	:= 		$(addprefix $(OBJ_DIR),${SRCS:.c=.o})

RM 		:= 		rm -f

NAME	:=		test

CC		:= 		cc

$(NAME): $(OBJ)
	$(CC) -o $@ $^

$(OBJ_DIR)%.o: $(SRC_DIR)%.c
	$(CC) -c -o $@ $^

all : ${NAME}

clean: 
	${RM} ${OBJ}

fclean: 	clean
	${RM} ${NAME}

re: 	fclean all

.PHONY:		all clean fclean re
