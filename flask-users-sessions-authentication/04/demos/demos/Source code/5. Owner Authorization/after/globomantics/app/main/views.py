from flask import Blueprint, render_template, session
from app.auth.views import current_user
from app.models import User, Role, Gig

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
	gigs = None
	if current_user.is_role(Role.MUSICIAN):
		gigs = Gig.query.all()
	return render_template('home.html', gigs=gigs)
