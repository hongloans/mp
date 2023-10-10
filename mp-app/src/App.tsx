import "./App.css";
import data from "../../test.json";

function App() {
  const dataList = Object.entries(data);
  return (
    <>
      <ul>
        {dataList.map(([keyv, valuev]) => {
          return <div>{keyv}</div>;
        })}
      </ul>
    </>
  );
}

export default App;
