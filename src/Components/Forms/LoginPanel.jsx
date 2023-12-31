import FormPanel from "./FormPanel";
import { useState } from "react";

export default function LoginPanel() {
  const EMAIL_URL = "email.com";
  const USERNAME_URL = "username.com";

  const [inputs, setInputs] = useState({
    username_email: "",
    password: "",
  });

  const isEmail = (email) => {
    return email.match(
      /^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$/gm,
    );
  };

  const onLogin = (e) => {
    e.preventDefault();

    console.log(isEmail(inputs.username_email));

    const url = isEmail(inputs.username_email) ? EMAIL_URL : USERNAME_URL;

    console.log(url);

    // fetch(url, {
    //   method: "POST",
    //   body: JSON.stringify(inputs),
    //   headers: {
    //     "Content-type": "application/json; charset=UTF-8",
    //   },
    // });
  };

  const handleChange = (e) => {
    const key = e.target.id;
    const value = e.target.value;
    setInputs((previousInputs) => ({ ...previousInputs, [key]: value }));
  };
  return (
    <FormPanel title="Login" onSubmit={onLogin}>
      <label htmlFor="email-username" className="font-bold">
        Email or Username
      </label>
      <input
        type="text"
        id="username_email"
        placeholder="Username or Email"
        value={inputs.username_email || ""}
        onChange={handleChange}
        className="border-2 border-gray-300 rounded-md p-1"
      />
      <label htmlFor="password" className="font-bold">
        Password
      </label>
      <input
        type="password"
        id="password"
        placeholder="Password"
        value={inputs.password || ""}
        onChange={handleChange}
        className="border-2 border-gray-300 rounded-md p-1"
      />
      <button
        className="w-1/2 self-center bg-blue-800 text-white p-2 text-lg rounded-2xl hover:bg-blue-700"
        type="submit"
      >
        Login
      </button>
      <p className="text-center">
        Don't have an account?{" "}
        <a href="/register" className="text-blue-800 hover:underline">
          Register
        </a>
      </p>
      <p className="text-center">
        Forgot your password?{" "}
        <a href="/reset-password" className="text-blue-800 hover:underline">
          Reset Password
        </a>
      </p>
    </FormPanel>
  );
}
