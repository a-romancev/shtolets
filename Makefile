.PHONY: run

run:
	nohup .env/bin/python3 manage.py runserver 0.0.0.0:80 0<&- &>/dev/null &