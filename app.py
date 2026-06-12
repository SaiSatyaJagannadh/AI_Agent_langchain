from flask import Flask, render_template, request, redirect, url_for, session
from agent import agent
import uuid

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route('/')
def home():

    # Create thread only once
    if 'thread_id' not in session:
        session['thread_id'] = str(uuid.uuid4())

    if 'messages' not in session:
        session['messages'] = []

    print("HOME SESSION:", dict(session))

    return render_template(
        'chat.html',
        messages=session['messages']
    )


@app.route('/send', methods=['POST'])
def send():

    user_message = request.form.get('message', '')

    user_lat = request.form.get('latitude')
    user_lon = request.form.get('longitude')
    print("FORM DATA:", request.form)
    print("LAT:", user_lat)
    print("LON:", user_lon)

    # Save location if browser sends it
    if user_lat and user_lon:

        session['user_location'] = {
            'lat': float(user_lat),
            'lon': float(user_lon)
        }

        print("LOCATION SAVED:", session['user_location'])

    print("SESSION BEFORE INVOKE:", dict(session))

    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            },
            {
                "configurable": {
                    "thread_id": session['thread_id']
                }
            }
        )

        ai_message = response['messages'][-1].content

    except Exception as e:

        print("AGENT ERROR:", e)

        ai_message = f"Error: {str(e)}"

    session['messages'].append(
        {
            'type': 'human',
            'content': user_message
        }
    )

    session['messages'].append(
        {
            'type': 'ai',
            'content': ai_message
        }
    )
    session.modified = True

    print("FINAL SESSION:", dict(session))

    return redirect(url_for('home'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)