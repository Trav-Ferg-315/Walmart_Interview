import json
from flask import Flask, render_template

URL = "https://api.github.com/repos/walmartlabs/thorax/issues"

# Retrives the data from the GitHub link
r = requests.get(url = URL)
data = r.json()
data2 = pd.DataFrame(data)

# Start of the website creation
app = Flask(__name__)

@app.route('/')
def index():
    
    rows = data2.hape[0]
    pageArr = pageArray(rows)

    # Takes the info for the First 10 files
    titles_df = data2[['title', 'number', 'state']][0:10]
    repoData = "walmart/thorax"

    # Assigns the first 10 to page 1
    currPage = 1

    return render_template('index.html', titles = titles_df.values, curr_pg = currPage, page_nums = pageArr, repo = repo_data)

@app.route('/<int:pageNum>')
def indexNum(pageNum):

    rows = data2.shape[0]
    pageArr = pageArray(rows)

    startEnd = pageIndex(pageNum, data2)
    titles_df = data2[['title', 'number', 'state']][startEnd[0]:startEnd[1]]
    repoData = "walmart/thorax"

    currPage = pageNum

    return render_template('index.html', titles = titles_df.values, curr_pg = currPage, page_nums = pageArr, repo = repo_data)

def pageArray(rows):
    pages = (rows // 10)
    pgsLeft = rows % 10

    if (pgsLeft > 0):
        pages += 1

    if (pages == 0):
        pages = 1

    arr = list(range(1, pages + 1))
    return arr

def pageIndex(pageNum, db):
    rows = db.shape[0]
    pageNum = rows // 10
    pageLast = rows % 10

    start = (pageNum - 1)*10
    end = start + 10
    arrFinal = [start, end]

    return arrFinal

    
if __name__ == "__main__":
    app.run()

