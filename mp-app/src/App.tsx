import "./App.css";
import data from "../../test.json";

function App() {
  const dataList = Object.entries(data);
  return (
    <>
      <ul>
        {dataList.map(([keyv, valuev]) => {
          return (<div>
            <h4>{keyv}</h4>
            <div dangerouslySetInnerHTML={{ __html: valuev }}></div>
          </div>);
        })}
      </ul>
    </>
  );
}

export default App;
