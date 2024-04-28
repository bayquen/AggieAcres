from flask import Flask, request, jsonify
from openai import OpenAI
app = Flask(__name__)

client = OpenAI(api_key="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")



# print(response.choices[0].message.content)
#
@app.route('/api/process-data', methods=['POST'])
def process_data():
    data = request.data.decode('utf-8')  # 解码为字符串
    if data:
        processed_data = handle_string_data(data)
        return jsonify({"status": "Data processed successfully", "processed_data": processed_data}), 200
    else:
        return jsonify({"error": "No data provided"}), 400

def handle_string_data(data):
    # 在这里实现您处理字符串的逻辑
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Address:4005 Cowell Blvd, Davis, CA 95618\nPrice:$2,200 - $2,749\nBeds:1-2 Beds\n\nAddress:3000 Lillard Dr, Davis, CA 95618\nPrice:$1,919 - $3,010\nBeds:1-2 Beds\n\nAddress:619 Pole Line Rd, Davis, CA 95618\nPrice:$1,505 - $3,460\nBeds:1-3 Beds\n\nAddress:606 Alvarado Ave, Davis, CA 95616\nPrice:$2,100 - $2,400\nBeds:2 Beds\n\nAddress:4141 Cowell Blvd, Davis, CA 95618\nPrice:$1,795 - $2,395\nBeds:1-2 Beds\n\nAddress:1850 Hanover Dr, Davis, CA 95616\nPrice:$2,240 - $2,675\nBeds:1-2 Beds\n\nAddress:4447 Cowell Blvd, Davis, CA 95618\nPrice:$2,050 - $2,825\nBeds:1-2 Beds\n\nAddress:801 D St, Davis, CA 95616\nPrice:$1,995 - $2,895\nBeds:1-2 Beds\n\nAddress:920 Cranbrook Ct, Davis, CA 95616\nPrice:$1,955 - $2,912\nBeds:1-2 Beds\n\nAddress:1959 Lake Blvd, Davis, CA 95616\nPrice:$620 - $3,495\nBeds:1-3 Beds\n\nAddress:1280 Olive Dr, Davis, CA 95616\nPrice:$2,195 - $2,625\nBeds:1-2 Beds\n\nAddress: 4005 Cowell Blvd, Davis, CA 95618\nPrice: $2,200 - $2,749\nBeds: 1-2 Beds\n\nAddress: 3000 Lillard Dr, Davis, CA 95618\nPrice: $1,919 - $3,010\nBeds: 1-2 Beds\n\nAddress: 1111 J St, Davis, CA 95616\nPrice: $1,800 - $2,100\nBeds: 1-2 Beds\n\nAddress: 619 Pole Line Rd, Davis, CA 95618\nPrice: $1,505 - $3,460\nBeds: 1-3 Beds\n\nAddress: 606 Alvarado Ave, Davis, CA 95616\nPrice: $2,100 - $2,400\nBeds: 2 Beds\n\nAddress: 4141 Cowell Blvd, Davis, CA 95618\nPrice: $1,795 - $2,395\nBeds: 1-2 Beds\n\nAddress: 801 J St, Davis, CA 95616\nPrice: $750 - $1,805\nBeds: 1-2 Beds\n\nAddress: 1850 Hanover Dr, Davis, CA 95616\nPrice: $2,240 - $2,675\nBeds: 1-2 Beds\n\nAddress: 4447 Cowell Blvd, Davis, CA 95618\nPrice: $2,050 - $2,825\nBeds: 1-2 Beds\n\nAddress: 801 D St, Davis, CA 95616\nPrice: $1,995 - $2,895\nBeds: 1-2 Beds\n\nAddress: 920 Cranbrook Ct, Davis, CA 95616\nPrice: $1,955 - $2,912\nBeds: 1-2 Beds\n\nAddress: 2689 Sycamore Ln, Davis, CA 95616\nPrice: $665 - $3,400\nBeds: 1-4 Beds\n\nAddress: 1959 Lake Blvd, Davis, CA 95616\nPrice: $620 - $3,495\nBeds: 1-3 Beds\n\nAddress: 2901 Portage Bay W, Davis, CA 95616\nPrice: $695 - $2,250\nBeds: 1-4 Beds\n\nAddress: 1280 Olive Dr, Davis, CA 95616\nPrice: $2,195 - $2,625\nBeds: 1-2 Beds\n\nYou are used to help users browse the data of houses next to the school and return the most suitable room for them based on the prompt given by the user. You need to recommend the user the most suitable one\nNow I will give you some houses. Please remember these houses. Later the user will enter a prompt. You have to tell him what you recommended, why you recommended it and the specific parameters of the recommended house."
            },
            {
                "role": "user",
                "content": data
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=25565)
