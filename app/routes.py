from flask import request, jsonify, request, render_template_string
from .services import jumble
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def configure_routes(app):
    #LIMT
    limiter = Limiter(app, key_func=get_remote_address)
    
    @app.route('/api/jumble/<int:n>', methods=['POST'])
    @limiter.limit("300 per minute")
    def api_jumble(n):
        print("Headers:", request.headers)  
        print("Body:", request.get_json())  
        data = request.get_json()
        message = data.get('message', '')
        if message:
            jumbled_message = jumble(message, n)
            return jsonify({"jumbled": jumbled_message})
        return jsonify({"error": "No message provided"}), 400
    

    @app.route('/', methods=['GET', 'POST'])
    def jumble_text():
        if request.method == 'POST':
            # Retrieve data from form
            input_text = request.form.get('input_text', '')
            shift_amount = request.form.get('shift_amount', 0, type=int)
            
            # Check for input completeness
            if input_text and shift_amount is not None:
                # Process the jumble function
                result = jumble(input_text, shift_amount)
                # Render result in an HTML template
                return render_template_string("""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Jumbled Result</title>
                    </head>
                    <body>
                        <h1>Jumbled Result: {{ result }}</h1>
                        <a href="/">Try another</a>
                    </body>
                    </html>
                """, result=result)
            else:
                return render_template_string("""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Error</title>
                    </head>
                    <body>
                        <h1>Error: Please provide both text and shift amount!</h1>
                        <a href="/">Back to form</a>
                    </body>
                    </html>
                """)
        else:
            # Render form [ get method]
            return render_template_string("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Jumble Text</title>
                </head>
                <body>
                    <form method="post">
                        <label for="input_text">Enter text:</label>
                        <input type="text" id="input_text" name="input_text" required>
                        <label for="shift_amount">Shift Amount:</label>
                        <input type="number" id="shift_amount" name="shift_amount" required>
                        <button type="submit">Jumble It!</button>
                    </form>
                </body>
                </html>
            """)
